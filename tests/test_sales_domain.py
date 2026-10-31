from __future__ import annotations

import pytest

from agents.sales_domain import (
    ContactabilityStatus,
    DemandEvidence,
    DemandSignal,
    DemandSignalType,
    EvidenceBasis,
    FactOrigin,
    FreshnessStatus,
    IdentityStatus,
    LeadQualification,
    MarketProfile,
    ProductFact,
    ProductFit,
    ProductProfile,
    ProductTaxonomy,
    SourceQuality,
    TaxonomyCategory,
    normalize_text,
    to_json_dict,
)


def page_evidence(**overrides):
    values = {
        "source_id": "source-1",
        "source_url": "https://example.org/public-post/1",
        "excerpt": "I am looking to buy a commercial fire alarm system.",
        "content_basis": EvidenceBasis.PAGE_TEXT,
        "publication_date": "2026-10-20",
        "event_date": None,
        "observed_at": "2026-10-31T08:00:00Z",
        "page_read": True,
    }
    values.update(overrides)
    return DemandEvidence(**values)


def test_normalize_text_handles_arabic_and_latin_without_changing_display_value():
    assert normalize_text("إِنذار الحَرِيق") == "انذار الحريق"
    assert normalize_text("Café, FIRE-ALARM") == "café fire-alarm"


def test_product_profile_requires_a_name_and_deduplicates_aliases():
    with pytest.raises(ValueError, match="name is required"):
        ProductProfile(name=" ")

    profile = ProductProfile(
        name="Fire Alarm Panel",
        aliases=("لوحة إنذار", "لوحه انذار", "FACP"),
    )

    assert profile.aliases == ("لوحة إنذار", "FACP")


def test_product_matching_uses_only_explicit_product_terms():
    profile = ProductProfile(
        name="Fire Alarm Panel",
        aliases=("لوحة إنذار الحريق", "FACP"),
    )

    assert profile.matching_terms("We need a FACP for a new building.") == ("FACP",)
    assert profile.matching_terms("نحتاج لوحة إنذار الحريق للمشروع") == ("لوحة إنذار الحريق",)
    assert profile.matching_terms("We need a fire alarm system.") == ()


def test_product_mention_does_not_create_demand_or_product_fit():
    profile = ProductProfile(
        name="Fire Alarm Panel",
        aliases=("Fire Alarm Panels",),
    )
    assert profile.matching_terms("The company sells Fire Alarm Panels.") == ("Fire Alarm Panels",)

    signal = DemandSignal(
        signal_id="signal-1",
        signal_type=DemandSignalType.UNKNOWN,
        evidence=page_evidence(),
    )

    assert signal.signal_type == DemandSignalType.UNKNOWN
    assert signal.product_fit == ProductFit.UNASSESSED


def test_product_taxonomy_is_caller_defined_and_supports_multiple_sectors():
    taxonomy = ProductTaxonomy(
        categories=(
            TaxonomyCategory(
                path=("safety", "fire_detection"),
                aliases=("fire alarm", "إنذار حريق"),
            ),
            TaxonomyCategory(
                path=("mobility", "vehicles"),
                aliases=("vehicle", "سيارة"),
            ),
            TaxonomyCategory(
                path=("construction", "residential_property"),
                aliases=("apartment", "شقة"),
            ),
        )
    )

    assert taxonomy.match_categories("نبحث عن إنذار حريق للمصنع") == (
        ("safety", "fire_detection"),
    )
    assert taxonomy.match_categories("vehicle and apartment") == (
        ("mobility", "vehicles"),
        ("construction", "residential_property"),
    )
    assert taxonomy.match_categories("unknown equipment") == ()


def test_taxonomy_does_not_match_partial_latin_words():
    taxonomy = ProductTaxonomy(
        categories=(
            TaxonomyCategory(path=("mobility", "cars"), aliases=("car",)),
        )
    )

    assert taxonomy.match_categories("carton packaging") == ()
    assert taxonomy.match_categories("used car") == (("mobility", "cars"),)


def test_taxonomy_rejects_duplicate_paths():
    first = TaxonomyCategory(path=("industry", "equipment"), aliases=("machine",))
    second = TaxonomyCategory(path=("industry", "equipment"), aliases=("device",))

    with pytest.raises(ValueError, match="paths must be unique"):
        ProductTaxonomy(categories=(first, second))


def test_source_verified_product_fact_requires_an_evidence_pointer():
    with pytest.raises(ValueError, match="require evidence_id"):
        ProductFact(
            field="operating_voltage",
            value="24V",
            origin=FactOrigin.SOURCE_VERIFIED,
        )

    fact = ProductFact(
        field="operating_voltage",
        value="24V",
        origin=FactOrigin.SOURCE_VERIFIED,
        evidence_id="manual-page-12",
    )
    assert fact.to_dict()["evidence_id"] == "manual-page-12"


def test_market_profile_is_a_constraint_not_a_demand_signal():
    market = MarketProfile(
        locations=("Egypt", "Cairo"),
        industries=("construction", "manufacturing"),
        customer_types=("contractor", "facility owner"),
        decision_roles=("procurement manager",),
        exclusions=("residential end users",),
    )

    assert market.to_dict()["industries"] == ["construction", "manufacturing"]
    assert not hasattr(market, "purchase_probability")


def test_buyer_query_generation_is_sector_neutral_and_product_anchored():
    from agents.sales_domain import build_buyer_queries

    vehicle = ProductProfile(name="سيارة كهربائية")
    industrial = ProductProfile(name="نظام إنذار حريق صناعي")
    vehicle_queries = build_buyer_queries(vehicle, locale="ar")
    industrial_queries = build_buyer_queries(industrial, locale="ar")

    assert vehicle_queries
    assert industrial_queries
    assert all("شقه" not in query and "تمليك" not in query for query in vehicle_queries)
    assert all("شقه" not in query and "تمليك" not in query for query in industrial_queries)
    assert any("سيارة كهربائية" in query for query in vehicle_queries)
    assert any("نظام انذار حريق صناعي" in query for query in industrial_queries)


def test_buyer_query_generation_uses_only_explicit_market_location():
    from agents.sales_domain import build_buyer_queries

    product = ProductProfile(name="FACP")
    market = MarketProfile(locations=("Cairo", "Egypt"))
    queries = build_buyer_queries(product, market, locale="en")

    assert queries
    assert all("Cairo Egypt" in query for query in queries)


def test_buyer_query_generation_drops_unrelated_planner_queries():
    from agents.sales_domain import build_buyer_queries

    product = ProductProfile(name="FACP")
    queries = build_buyer_queries(
        product,
        locale="en",
        existing_queries=(
            "apartments for sale in Cairo",
            "FACP procurement request",
            "generic buying intent",
        ),
    )

    assert any("FACP procurement request" in query for query in queries)
    assert all("apartments" not in query for query in queries)
    assert all("generic buying intent" not in query for query in queries)

def test_demand_evidence_requires_an_absolute_http_url():
    with pytest.raises(ValueError, match="absolute HTTP"):
        page_evidence(source_url="/relative/path")

    with pytest.raises(ValueError, match="embedded credentials"):
        page_evidence(source_url="https://user:secret@example.org/post")


def test_demand_evidence_keeps_publication_event_and_observation_dates_separate():
    evidence = page_evidence(
        publication_date="2026-10-20",
        event_date="2026-10-18",
        observed_at="2026-10-31T08:00:00+02:00",
    )

    assert evidence.publication_date == "2026-10-20"
    assert evidence.event_date == "2026-10-18"
    assert evidence.observed_at == "2026-10-31T08:00:00+02:00"


@pytest.mark.parametrize("field", ["publication_date", "event_date"])
def test_demand_evidence_rejects_invalid_dates(field):
    with pytest.raises(ValueError, match="ISO date"):
        page_evidence(**{field: "yesterday"})


def test_demand_evidence_does_not_invent_missing_dates():
    evidence = page_evidence(
        publication_date=None,
        event_date=None,
        observed_at=None,
    )

    assert evidence.publication_date is None
    assert evidence.event_date is None
    assert evidence.observed_at is None


def test_observation_timestamp_requires_timezone():
    with pytest.raises(ValueError, match="timezone offset"):
        page_evidence(observed_at="2026-10-31T08:00:00")


def test_search_snippet_cannot_be_labelled_as_a_read_page():
    with pytest.raises(ValueError, match="cannot be marked"):
        page_evidence(
            content_basis=EvidenceBasis.SEARCH_SNIPPET,
            page_read=True,
        )


def test_page_text_requires_successful_page_read():
    with pytest.raises(ValueError, match="requires page_read"):
        page_evidence(
            content_basis=EvidenceBasis.PAGE_TEXT,
            page_read=False,
        )


def test_title_and_snippet_evidence_can_remain_unread():
    title = page_evidence(
        content_basis=EvidenceBasis.TITLE,
        page_read=False,
    )
    snippet = page_evidence(
        content_basis=EvidenceBasis.SEARCH_SNIPPET,
        page_read=False,
    )

    assert title.page_read is False
    assert snippet.page_read is False


def test_demand_type_and_product_fit_are_independent():
    signal = DemandSignal(
        signal_id="signal-direct",
        signal_type=DemandSignalType.DIRECT_PURCHASE_REQUEST,
        evidence=page_evidence(),
        product_fit=ProductFit.UNASSESSED,
        classification_reason="The source explicitly asks to buy.",
    )

    assert signal.signal_type == DemandSignalType.DIRECT_PURCHASE_REQUEST
    assert signal.product_fit == ProductFit.UNASSESSED
    assert signal.identity_status == IdentityStatus.UNKNOWN


def test_assessed_product_fit_requires_a_rationale():
    with pytest.raises(ValueError, match="requires a rationale"):
        DemandSignal(
            signal_id="signal-fit",
            signal_type=DemandSignalType.STATED_NEED,
            evidence=page_evidence(),
            product_fit=ProductFit.FIT,
        )

    signal = DemandSignal(
        signal_id="signal-fit",
        signal_type=DemandSignalType.STATED_NEED,
        evidence=page_evidence(),
        product_fit=ProductFit.FIT,
        product_fit_reason="The requested specification matches the product profile.",
    )
    assert signal.product_fit == ProductFit.FIT


def test_unassessed_product_fit_must_not_have_a_rationale():
    with pytest.raises(ValueError, match="must not have a fit rationale"):
        DemandSignal(
            signal_id="signal-unassessed",
            signal_type=DemandSignalType.INDIRECT_INDICATOR,
            evidence=page_evidence(),
            product_fit_reason="No assessment has been made.",
        )


def test_icp_match_only_remains_distinct_from_direct_purchase():
    signal = DemandSignal(
        signal_id="signal-icp",
        signal_type=DemandSignalType.ICP_MATCH_ONLY,
        evidence=page_evidence(
            excerpt="A business in the target industry operates in Cairo.",
            content_basis=EvidenceBasis.TITLE,
            page_read=False,
        ),
    )

    assert signal.signal_type == DemandSignalType.ICP_MATCH_ONLY
    assert signal.signal_type != DemandSignalType.DIRECT_PURCHASE_REQUEST


def test_lead_qualification_exposes_independent_dimensions_without_probability():
    assessment = LeadQualification(
        signal_id="signal-1",
        product_fit=ProductFit.FIT,
        source_quality=SourceQuality.PRIMARY_SOURCE,
        freshness=FreshnessStatus.CURRENT,
        identity_status=IdentityStatus.UNVERIFIED,
        contactability=ContactabilityStatus.NOT_ASSESSED,
        missing_information=("buyer identity", "public contact channel"),
    )

    result = assessment.to_dict()
    assert result["product_fit"] == "fit"
    assert result["source_quality"] == "primary_source"
    assert result["freshness"] == "current"
    assert result["identity_status"] == "unverified"
    assert result["missing_information"] == ["buyer identity", "public contact channel"]
    assert "purchase_probability" not in result
    assert "confidence" not in result


def test_to_json_dict_preserves_all_evidence_provenance_fields():
    evidence = page_evidence(event_date="2026-10-18")
    serialized = to_json_dict(evidence)

    assert serialized["source_url"] == "https://example.org/public-post/1"
    assert serialized["content_basis"] == "page_text"
    assert serialized["publication_date"] == "2026-10-20"
    assert serialized["event_date"] == "2026-10-18"
    assert serialized["observed_at"] == "2026-10-31T08:00:00Z"
    assert serialized["page_read"] is True


def test_domain_models_reject_invalid_sequence_types():
    with pytest.raises(TypeError, match="iterable of strings"):
        ProductProfile(name="Product", aliases="one alias")

    with pytest.raises(TypeError, match="TaxonomyCategory instances"):
        ProductTaxonomy(categories=("property",))


def test_contactability_is_not_inferred_from_identity():
    assessment = LeadQualification(
        signal_id="signal-contact",
        identity_status=IdentityStatus.VERIFIED,
    )

    assert assessment.identity_status == IdentityStatus.VERIFIED
    assert assessment.contactability == ContactabilityStatus.NOT_ASSESSED
