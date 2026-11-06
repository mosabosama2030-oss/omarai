import csv

import pytest

from agents.omarai import LeadStore, analyze, normalize


def test_arabic_normalization():
    assert normalize("إيجارٌ ـ شقة") == normalize("ايجار شقة")

def test_high_intent_with_next_step():
    result=analyze("بدور على شقة وممكن معاينة")
    assert result["label"]=="high_intent"
    assert result["score"]>=55

def test_non_buyer_override():
    result=analyze("مش عايز اشتري، عايز ابيع شقة")
    assert result["label"]=="not_buyer_signal"
    assert result["score"]==0

def test_empty_text_rejected():
    with pytest.raises(ValueError):
        analyze(" ")

def test_url_required_and_validated(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    with pytest.raises(ValueError):
        store.add("بدور على شقة","","manual")
    with pytest.raises(ValueError):
        store.add("بدور على شقة","file:///tmp/private","manual")

def test_duplicate_is_idempotent(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    one,created1=store.add("بدور على شقة","https://example.com/post/1","facebook")
    two,created2=store.add("بدور على شقة","https://example.com/post/1","facebook")
    assert created1 is True and created2 is False
    assert one["id"]==two["id"]
    assert len(store.list())==1

def test_status_updates_are_explicit(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    lead,_=store.add("بدور على شقة","https://example.com/p","manual")
    updated=store.update_status(lead["id"],"qualified")
    assert updated["status"]=="qualified"
    with pytest.raises(ValueError):
        store.update_status(lead["id"],"magic")

def test_csv_requires_columns(tmp_path):
    bad=tmp_path/"bad.csv"
    bad.write_text("foo,bar\na,b\n",encoding="utf-8")
    store=LeadStore(tmp_path/"db.sqlite3")
    with pytest.raises(ValueError):
        store.import_csv(bad)

def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):
    store = LeadStore(tmp_path / "db.sqlite3")
    store.add(
        '=HYPERLINK("https://evil.example","click")',
        "https://example.com/post/1",
        platform="manual",
        note="  +SUM(1,1)",
    )
    store.add(
        "\u00a0\ufeff=1+1",
        "https://example.com/post/2",
        platform="manual",
        note="\u00a0\ufeff=SUM(1,1)",
    )
    destination = tmp_path / "export.csv"
    assert store.export_csv(destination) == 2
    raw_csv = destination.read_text(encoding="utf-8-sig")
    assert '"\t=HYPERLINK(' in raw_csv
    assert '"\t  +SUM' in raw_csv

    with destination.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))

    row1 = next(row for row in rows if row["source_url"] == "https://example.com/post/1")
    row2 = next(row for row in rows if row["source_url"] == "https://example.com/post/2")
    assert row1["text"].startswith("\t=")
    assert row1["note"].startswith("\t  +")
    assert row2["text"].startswith("\t\ufeff=")
    assert row2["note"].startswith("\t\u00a0\ufeff=")



def test_generic_fire_alarm_and_supplier_requests_are_sector_neutral():
    fire_alarm = analyze("نحتاج نظام إنذار حريق للمصنع")
    supplier = analyze("نبحث عن مورد لافتات لمشروع جديد")
    assert fire_alarm["label"] == "high_intent"
    assert supplier["label"] == "high_intent"
    assert fire_alarm["score"] >= 55
    assert supplier["score"] >= 55


def test_product_mention_alone_does_not_create_a_demand_signal():
    result = analyze("نظام إنذار حريق")
    assert result["label"] == "unclear"
    assert result["score"] == 0


@pytest.mark.parametrize(
    "text",
    [
        "مش بدور على شقة",
        "مش محتاج نظام إنذار حريق",
        "لا نحتاج مورد لافتات",
        "not looking for a supplier",
        "we do not need a fire alarm system",
    ],
)
def test_explicit_negation_never_scores_as_buyer_intent(text):
    result = analyze(text)
    assert result["label"] == "not_buyer_signal"
    assert result["score"] == 0


@pytest.mark.parametrize(
    "text",
    [
        "تم الشراء بالفعل",
        "وجدنا مورد وتم التعاقد",
        "already purchased the equipment",
        "supplier selected",
        "كنت بدور على شقة",
    ],
)
def test_completed_or_past_need_is_not_active_demand(text):
    result = analyze(text)
    assert result["label"] == "closed_or_stale_signal"
    assert result["score"] == 0


def test_product_and_location_context_do_not_inflate_demand_score():
    result = analyze(
        "نظام إنذار حريق في القاهرة",
        product_terms=["نظام إنذار حريق"],
        location_terms=["القاهرة"],
    )
    assert result["score"] == 0
    assert result["label"] == "unclear"
    assert {item["category"] for item in result["matched_signals"]} == {
        "product_context",
        "location_context",
    }
