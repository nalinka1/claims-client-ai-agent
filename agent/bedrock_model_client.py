from typing import Any
import boto3


class BedrockModelClient:

    def __init__(self, model_id: str, region_name: str):
        self.model_id = model_id

        self.client = boto3.client(
            "bedrock-runtime",
            region_name=region_name
        )

    def generate(
        self,
        system_prompt: str,
        messages: list[dict],
        tools: list[dict] | None = None
    ) -> dict[str, Any]:

        bedrock_messages = []

        for message in messages:
            content = message["content"]

            if isinstance(content, str):
                content = [{"text": content}]

            bedrock_messages.append({
                "role": message["role"],
                "content": content
            })

        request = {
            "modelId": self.model_id,
            "system": [
                {"text": system_prompt}
            ],
            "messages": bedrock_messages
        }

        if tools:
            request["toolConfig"] = {
                "tools": tools
            }

        response = self.client.converse(**request)

        return response