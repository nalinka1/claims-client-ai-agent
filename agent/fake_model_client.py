from agent.model_client import ModelClient


class FakeModelClient:

    def generate(self, prompt: str) -> str:
        return f"Fake model response for: {prompt}"