from agent.claims_agent import ClaimsAgent
from agent.fake_model_client import FakeModelClient


def test_agent_returns_model_response():
    model_client = FakeModelClient()
    agent = ClaimsAgent(model_client)

    response = agent.respond("What documents can I provide?")

    assert response == "Fake model response for: What documents can I provide?"