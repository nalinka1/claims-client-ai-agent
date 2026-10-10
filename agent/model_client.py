from typing import Any, Protocol


class ModelClient(Protocol):

 def generate(
        self,
        system_prompt: str,
        messages: list[dict],
        tools: list[dict] | None = None
    ) -> dict[str, Any]:
        ...