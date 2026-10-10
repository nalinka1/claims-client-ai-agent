import os

from agent.bedrock_model_client import BedrockModelClient
from agent.claims_agent import ClaimsAgent

def main():
    model_client = BedrockModelClient(
            model_id=os.environ["BEDROCK_MODEL_ID"],
            region_name=os.environ["AWS_REGION"],
        )

    agent = ClaimsAgent(model_client)

    print("Demo Claims Services Assistant")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() == "exit":
            break

        response = agent.respond(user_message)

        print(f"\nAssistant: {response}\n")



if __name__ == "__main__":
    main()