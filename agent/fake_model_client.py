from agent.model_client import ModelClient


class FakeModelClient:

    def generate(self, system_prompt: str, prompt: str) -> str:
        return f"Fake model response for: {prompt}"