from typing import Any

def generate(
    self,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None
) -> dict[str, Any]:

    bedrock_messages = []

    for message in messages:
        content = message["content"]

        # Convert simple text messages into Bedrock format.
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

    # Include tool definitions only when provided.
    if tools:
        request["toolConfig"] = {
            "tools": tools
        }

    response = self.client.converse(**request)

    return response