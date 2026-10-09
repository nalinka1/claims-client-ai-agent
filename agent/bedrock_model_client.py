import boto3

from agent.model_client import ModelClient


class BedrockModelClient:

    def __init__(self, model_id: str, region_name: str):
        self.model_id = model_id
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=region_name,
        )

    def generate(self, system_prompt: str, prompt: str) -> str:
        response = self.client.converse(
            modelId=self.model_id,
            system=[
                {
                "text": system_prompt
                }
                ],
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ],
                }
            ],
        )

        return response["output"]["message"]["content"][0]["text"]