# tests/test_llm_client.py
import os
import pytest

from src.llm_client import LLMClient


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set",
)
def test_openai_hello_world():
    client = LLMClient(provider="openai")
    out = client.generate("Say 'Hello world' and nothing else.")
    assert "hello world" in out.lower()


@pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"),
    reason="ANTHROPIC_API_KEY not set",
)
def test_anthropic_hello_world():
    client = LLMClient(provider="anthropic")
    out = client.generate("Say 'Hello world' and nothing else.")
    assert "hello world" in out.lower()
