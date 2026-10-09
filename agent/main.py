from agent.fake_model_client import FakeModelClient
from agent.claims_agent import ClaimsAgent

def main():
    model_client = FakeModelClient()
    agent = ClaimsAgent(model_client)

    response = agent.respond("What documents can I provide for my claim?")

    print(response)


if __name__ == "__main__":
    main()