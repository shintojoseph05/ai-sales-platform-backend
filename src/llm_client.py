# src/llm_client.py
import os
from typing import Literal, Optional

from openai import OpenAI  # pip install openai
from anthropic import Anthropic  # pip install anthropic


Provider = Literal["openai", "anthropic"]


class LLMClient:
    def __init__(
        self,
        provider: Provider = "openai",
        model: Optional[str] = None,
    ) -> None:
        self.provider = provider

        if provider == "openai":
            # Uses OPENAI_API_KEY from env by default
            self.client = OpenAI()  # type: ignore[call-arg]
            self.model = model or "gpt-4o"
        elif provider == "anthropic":
            # Uses ANTHROPIC_API_KEY from env by default
            self.client = Anthropic()  # type: ignore[call-arg]
            self.model = model or "claude-sonnet-4-20250514"
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def generate(self, prompt: str) -> str:
        if self.provider == "openai":
            resp = self.client.responses.create(  # type: ignore[attr-defined]
                model=self.model,
                input=prompt,
            )
            # SDK exposes convenience property for text
            return resp.output_text  # type: ignore[attr-defined]

        if self.provider == "anthropic":
            resp = self.client.messages.create(  # type: ignore[attr-defined]
                model=self.model,
                max_tokens=256,
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            # Anthropic returns a list of content blocks, usually first is text
            parts = resp.content  # type: ignore[attr-defined]
            if not parts:
                return ""
            first = parts[0]
            # For text blocks, .text holds the string
            return getattr(first, "text", str(first))

        raise RuntimeError("Invalid provider state")
