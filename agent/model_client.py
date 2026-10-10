from typing import Protocol


class ModelClient(Protocol):

    def generate(self, system_prompt: str, messages: list[dict]) -> str:
        ...