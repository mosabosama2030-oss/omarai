FROM python:3.12-slim

ARG OMARAI_BUILD_SHA=unknown
ARG PUBLIC_OMARAI_BUILD_SHA=unknown
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
COPY pyproject.toml README.md ./
COPY agents ./agents
COPY api ./api
COPY cli ./cli
COPY web ./web

RUN python -m pip install --no-cache-dir .
RUN python -c "import os; from pathlib import Path; import api.omarai; values=(os.getenv('OMARAI_BUILD_SHA',''), os.getenv('PUBLIC_OMARAI_BUILD_SHA','')); valid=lambda value: len(value.strip())==40 and all(char in '0123456789abcdef' for char in value.strip().lower()); sha=next((value.strip().lower() for value in values if valid(value)), 'unknown'); Path(api.omarai.__file__).resolve().parents[1].joinpath('BUILD_SHA').write_text(sha, encoding='ascii')"

EXPOSE 8000
CMD ["sh", "-c", "python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}"]
