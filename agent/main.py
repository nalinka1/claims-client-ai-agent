import os

from agent.bedrock_model_client import BedrockModelClient
from agent.claims_agent import ClaimsAgent

def main():
    model_client = BedrockModelClient(
            model_id=os.environ["BEDROCK_MODEL_ID"],
            region_name=os.environ["AWS_REGION"],
        )

    agent = ClaimsAgent(model_client)

    #response = agent.respond("What is a claim?")
    response = agent.respond(
    "My claim number is CLM-12345. "
    "Can you check whether my claim has been approved?")

    print(response)



if __name__ == "__main__":
    main()