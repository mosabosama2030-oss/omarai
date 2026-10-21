FROM python:3.12-slim

ARG OMARAI_BUILD_SHA=unknown
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
RUN printf '%s\n' "$OMARAI_BUILD_SHA" > /app/BUILD_SHA
COPY pyproject.toml README.md ./
COPY agents ./agents
COPY api ./api
COPY cli ./cli
COPY web ./web

RUN python -m pip install --no-cache-dir .

EXPOSE 8000
CMD ["sh", "-c", "python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}"]
