from typing import Protocol


class ModelClient(Protocol):

    def generate(self, system_prompt: str, prompt: str) -> str:
        ...