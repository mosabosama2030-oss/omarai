from pathlib import Path

DOCKERFILE = (Path(__file__).resolve().parents[1] / "Dockerfile").read_text(encoding="utf-8")


def test_dockerfile_declares_healthcheck_on_public_health_endpoint():
    assert "HEALTHCHECK" in DOCKERFILE
    assert "/api/health" in DOCKERFILE.split("HEALTHCHECK", 1)[1]
    assert "PORT" in DOCKERFILE.split("HEALTHCHECK", 1)[1].split("CMD [\"sh\", \"-c\", \"python -m", 1)[0]
