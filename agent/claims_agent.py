from agent.model_client import ModelClient


class ClaimsAgent:
    def __init__(self, model_client: ModelClient):
        self.model_client = model_client

    def respond(self, user_message: str) -> str:
        return self.model_client.generate(user_message)
