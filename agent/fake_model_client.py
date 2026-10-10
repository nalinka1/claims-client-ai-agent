from agent.model_client import ModelClient


class FakeModelClient:

    def generate(
        self,
        system_prompt: str,
        messages: list[dict]
    ) -> str:
        last_message = messages[-1]["content"]
        return f"Fake response to: {last_message}"