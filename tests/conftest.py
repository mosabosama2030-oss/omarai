"""Test defaults: keep mocked offline tests free of the optional extra model call."""
import os

# The knowledge-first stage makes one additional model request per web answer.
# Existing mocked pipelines assert exact model prompts/diagnostics, so tests opt in.
os.environ.setdefault("OMARAI_KNOWLEDGE_FIRST", "0")
