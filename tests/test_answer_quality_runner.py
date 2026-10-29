"""Offline tests for scripts/run_answer_quality_benchmark.py (no network)."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_answer_quality_benchmark.py"
CORPUS = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"


def _load_runner():
    spec = importlib.util.spec_from_file_location("aq_runner", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["aq_runner"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_runner_script_exists():
    assert SCRIPT.is_file()


def test_validate_mode_succeeds_on_real_corpus(capsys):
    mod = _load_runner()
    rc = mod.main(["--mode", "validate", "--corpus", str(CORPUS), "--summary"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "VALIDATE OK" in out
    assert "NOT_TESTED" in out


def test_validate_rejects_missing_file(tmp_path):
    mod = _load_runner()
    missing = tmp_path / "nope.json"
    with pytest.raises(FileNotFoundError):
        mod.load_corpus(missing)


def test_validate_detects_bad_case_count(tmp_path):
    mod = _load_runner()
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    data["case_count"] = 999
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    problems = mod.validate_corpus(mod.load_corpus(bad))
    assert any("case_count" in p for p in problems)


def test_validate_detects_missing_required_field(tmp_path):
    mod = _load_runner()
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    data["cases"] = [dict(data["cases"][0])]
    del data["cases"][0]["question"]
    data["case_count"] = 1
    bad = tmp_path / "bad2.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    problems = mod.validate_corpus(mod.load_corpus(bad))
    assert problems


def test_live_refuses_unbounded_without_limit_or_case_id(capsys):
    mod = _load_runner()
    rc = mod.main(["--mode", "live", "--corpus", str(CORPUS)])
    assert rc == 2
    err = capsys.readouterr().err
    assert "Refusing unbounded" in err


def test_live_unknown_case_id(capsys):
    mod = _load_runner()
    rc = mod.main(
        [
            "--mode",
            "live",
            "--corpus",
            str(CORPUS),
            "--case-id",
            "AQ-999",
            "--base-url",
            "http://127.0.0.1:9",
        ]
    )
    assert rc == 2


def test_redact_secrets_strips_token_value(monkeypatch):
    mod = _load_runner()
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "super-secret-token-value-xyz")
    text = "token=super-secret-token-value-xyz and OPENROUTER_API_KEY"
    out = mod.redact_secrets(text)
    assert "super-secret-token-value-xyz" not in out
    assert "REDACTED" in out


def test_live_records_not_tested_not_pass(monkeypatch, tmp_path, capsys):
    """Even on HTTP 200, quality status stays NOT_TESTED (no keyword auto-PASS)."""
    mod = _load_runner()

    def fake_post(base_url, question, timeout, token):
        return 200, {
            "answer": "hello used_web_search should not force PASS",
            "used_web_search": False,
            "used_language_model": True,
            "sources": [],
        }

    monkeypatch.setattr(mod, "get_verified_build_sha", lambda base_url, timeout, token=None: "a" * 40)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    out = tmp_path / "results.json"
    rc = mod.main(
        [
            "--mode",
            "live",
            "--corpus",
            str(CORPUS),
            "--case-id",
            "AQ-001",
            "--limit",
            "1",
            "--out",
            str(out),
        ]
    )
    assert rc == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["results"][0]["status"] == "NOT_TESTED"
    assert payload["results"][0]["evidence_fixture_injected"] is False
    assert payload["results"][0]["transport_ok"] is True
    assert payload["build_sha"] == "a" * 40
    assert payload["build_sha_verification"] == "confirmed_by_api_health"


def test_validate_base_url_rejects_non_loopback_http():
    mod = _load_runner()
    with pytest.raises(ValueError, match="Plain HTTP"):
        mod.validate_base_url("http://research.example")


@pytest.mark.parametrize(
    "url",
    [
        "https://user:password@example.com",
        "https://example.com/private/path",
        "https://example.com/?token=oops",
        "https://example.com/#fragment",
    ],
)
def test_validate_base_url_rejects_ambiguous_or_credential_bearing_urls(url):
    mod = _load_runner()
    with pytest.raises(ValueError):
        mod.validate_base_url(url)


def test_remote_bearer_token_requires_exact_allowlisted_https_origin(monkeypatch):
    mod = _load_runner()
    monkeypatch.delenv("OMARAI_BENCHMARK_ALLOWED_ORIGIN", raising=False)
    with pytest.raises(ValueError, match="OMARAI_BENCHMARK_ALLOWED_ORIGIN"):
        mod.validate_base_url("https://app.example", token_present=True)

    monkeypatch.setenv("OMARAI_BENCHMARK_ALLOWED_ORIGIN", "https://app.example")
    assert mod.validate_base_url("https://app.example/", token_present=True) == "https://app.example"
    with pytest.raises(ValueError, match="does not match"):
        mod.validate_base_url("https://other.example", token_present=True)


def test_remote_token_origin_comparison_normalizes_default_https_port(monkeypatch):
    mod = _load_runner()
    monkeypatch.setenv("OMARAI_BENCHMARK_ALLOWED_ORIGIN", "https://app.example")
    assert (
        mod.validate_base_url("https://app.example:443", token_present=True)
        == "https://app.example"
    )


def test_redirect_handler_refuses_following_redirects():
    mod = _load_runner()
    handler = mod._NoRedirectHandler()
    assert handler.redirect_request(
        req=None,
        fp=None,
        code=302,
        msg="Found",
        headers={},
        newurl="https://attacker.example/collect",
    ) is None


def test_live_rejects_unapproved_remote_url_before_network(monkeypatch, capsys):
    mod = _load_runner()
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "a-test-token")
    monkeypatch.delenv("OMARAI_BENCHMARK_ALLOWED_ORIGIN", raising=False)
    rc = mod.run_live(
        CORPUS,
        "https://not-allowlisted.example",
        "AQ-001",
        1,
        1.0,
        0.0,
        None,
    )
    assert rc == 2
    assert "Unsafe base URL" in capsys.readouterr().err


def test_live_transport_error_still_not_pass(monkeypatch, tmp_path):
    mod = _load_runner()

    def fake_post(base_url, question, timeout, token):
        return 0, {"error": "URLError", "detail": "connection refused"}

    monkeypatch.setattr(mod, "get_verified_build_sha", lambda base_url, timeout, token=None: "b" * 40)
    monkeypatch.setattr(mod, "get_verified_build_sha", lambda base_url, timeout, token=None: "b" * 40)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    out = tmp_path / "results.json"
    rc = mod.main(
        [
            "--mode",
            "live",
            "--corpus",
            str(CORPUS),
            "--case-id",
            "AQ-001",
            "--out",
            str(out),
        ]
    )
    assert rc == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["results"][0]["status"] == "NOT_TESTED"
    assert payload["results"][0]["transport_ok"] is False



def test_response_metrics_separates_tool_status_from_http_success():
    mod = _load_runner()
    failed_search = mod._response_metrics(
        {
            "search_report": {"search_outcome": "attempted_research_error"},
            "sources": [],
        },
        expected_strategy="web_search",
        transport_ok=True,
    )
    assert failed_search["tool_status"] == "TOOL_FAILED"
    assert failed_search["request_cost_usd"] is None
    assert failed_search["request_cost_status"] == "NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED"

    successful_search = mod._response_metrics(
        {
            "search_report": {
                "search_outcome": "attempted_with_usable_sources",
                "pipeline_completion_status": "completed",
                "model_calls": [{
                    "requested_model": "test/model",
                    "provider_usage": {
                        "prompt_tokens": 10,
                        "completion_tokens": 20,
                        "total_tokens": 30,
                        "cost_usd": 0.0008,
                    },
                }],
            },
            "model_calls": [],
            "sources": [{"url": "https://example.org"}],
        },
        expected_strategy="web_search",
        transport_ok=True,
    )
    assert successful_search["tool_status"] == "SUCCESS_WITH_USABLE_RESULTS"
    assert successful_search["source_count"] == 1
    assert successful_search["provider_reported_model_cost_usd"] == 0.0008
    assert successful_search["provider_reported_model_cost_status"] == "COMPLETE_FOR_RETURNED_MODEL_CALLS"


def test_request_cost_ledger_accepts_explicit_full_request_usd_reconciliation(tmp_path):
    mod = _load_runner()
    ledger_path = tmp_path / "cost-ledger.json"
    ledger_path.write_text(
        json.dumps({
            "schema_version": "1.0",
            "currency": "USD",
            "scope": "complete_request",
            "source": "provider usage export reviewed by operator",
            "costs": [{"case_id": "AQ-001", "cost_usd": 0.0042}],
        }),
        encoding="utf-8",
    )
    costs, source = mod._load_request_cost_ledger(ledger_path, {"AQ-001", "AQ-002"})
    assert costs == {"AQ-001": 0.0042}
    assert source == "provider usage export reviewed by operator"


@pytest.mark.parametrize(
    "ledger, allowed_ids, message",
    [
        ({"currency": "EUR", "scope": "complete_request", "source": "invoice", "costs": []}, {"AQ-001"}, "currency=USD"),
        ({"currency": "USD", "scope": "model_only", "source": "invoice", "costs": []}, {"AQ-001"}, "scope=complete_request"),
        ({"currency": "USD", "scope": "complete_request", "source": "", "costs": []}, {"AQ-001"}, "non-empty source"),
        ({"currency": "USD", "scope": "complete_request", "source": "invoice", "costs": [{"case_id": "AQ-404", "cost_usd": 0.0}]}, {"AQ-001"}, "unknown case_id"),
        ({"currency": "USD", "scope": "complete_request", "source": "invoice", "costs": [{"case_id": "AQ-001", "cost_usd": -0.1}]}, {"AQ-001"}, "finite and non-negative"),
    ],
)
def test_request_cost_ledger_rejects_unverifiable_values(tmp_path, ledger, allowed_ids, message):
    mod = _load_runner()
    path = tmp_path / "cost-ledger.json"
    path.write_text(json.dumps(ledger), encoding="utf-8")
    with pytest.raises(ValueError, match=message):
        mod._load_request_cost_ledger(path, allowed_ids)


def test_live_refuses_build_sha_mismatch_before_posting(monkeypatch, capsys):
    mod = _load_runner()
    calls = []

    def fake_post(base_url, question, timeout, token):
        calls.append(question)
        return 200, {"answer": "must not run"}

    monkeypatch.setattr(mod, "get_verified_build_sha", lambda base_url, timeout, token=None: "a" * 40)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    rc = mod.run_live(
        CORPUS, "http://127.0.0.1:8765", "AQ-001", 1, 1.0, 0.0, None,
        build_sha="b" * 40,
    )
    assert rc == 2
    assert calls == []
    assert "Build SHA mismatch" in capsys.readouterr().err


def test_live_refuses_unknown_health_build_sha_before_posting(monkeypatch, capsys):
    mod = _load_runner()
    calls = []

    def fake_post(base_url, question, timeout, token):
        calls.append(question)
        return 200, {"answer": "must not run"}

    def unknown_sha(base_url, timeout, token=None):
        raise ValueError("/api/health build.sha is missing or not a full 40-character SHA")

    monkeypatch.setattr(mod, "get_verified_build_sha", unknown_sha)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    rc = mod.run_live(
        CORPUS, "http://127.0.0.1:8765", "AQ-001", 1, 1.0, 0.0, None,
    )
    assert rc == 2
    assert calls == []
    assert "Unverified deployed build" in capsys.readouterr().err


def test_get_verified_build_sha_requires_full_api_health_identity(monkeypatch):
    mod = _load_runner()
    import json

    class FakeResponse:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

        def read(self, limit):
            return json.dumps({"ok": True, "build": {"sha": "C" * 40}}).encode("utf-8")

    monkeypatch.setattr(mod._NO_REDIRECT_OPENER, "open", lambda request, timeout: FakeResponse())
    assert mod.get_verified_build_sha("http://127.0.0.1:8765", 1.0) == "c" * 40


def test_live_refuses_build_sha_mismatch_before_posting(monkeypatch, capsys):
    mod = _load_runner()
    calls = []

    def fake_post(base_url, question, timeout, token):
        calls.append(question)
        return 200, {"answer": "must not run"}

    monkeypatch.setattr(mod, "get_verified_build_sha", lambda base_url, timeout, token=None: "a" * 40)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    rc = mod.run_live(
        CORPUS, "http://127.0.0.1:8765", "AQ-001", 1, 1.0, 0.0, None,
        build_sha="b" * 40,
    )
    assert rc == 2
    assert calls == []
    assert "Build SHA mismatch" in capsys.readouterr().err


def test_live_refuses_unknown_health_build_sha_before_posting(monkeypatch, capsys):
    mod = _load_runner()
    calls = []

    def fake_post(base_url, question, timeout, token):
        calls.append(question)
        return 200, {"answer": "must not run"}

    def unknown_sha(base_url, timeout, token=None):
        raise ValueError("/api/health build.sha is missing or not a full 40-character SHA")

    monkeypatch.setattr(mod, "get_verified_build_sha", unknown_sha)
    monkeypatch.setattr(mod, "post_agent", fake_post)
    rc = mod.run_live(
        CORPUS, "http://127.0.0.1:8765", "AQ-001", 1, 1.0, 0.0, None,
    )
    assert rc == 2
    assert calls == []
    assert "Unverified deployed build" in capsys.readouterr().err


def test_get_verified_build_sha_requires_full_api_health_identity(monkeypatch):
    mod = _load_runner()

    class FakeResponse:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

        def read(self, limit):
            return json.dumps({"ok": True, "build": {"sha": "C" * 40}}).encode("utf-8")

    monkeypatch.setattr(mod._NO_REDIRECT_OPENER, "open", lambda request, timeout: FakeResponse())
    assert mod.get_verified_build_sha("http://127.0.0.1:8765", 1.0) == "c" * 40
