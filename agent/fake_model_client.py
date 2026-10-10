from typing import Any


class FakeModelClient:

    def generate(
        self,
        system_prompt: str,
        messages: list[dict],
        tools: list[dict] | None = None
    ) -> dict[str, Any]:

        last_message = messages[-1]["content"]

        return {
            "stopReason": "end_turn",
            "output": {
                "message": {
                    "role": "assistant",
                    "content": [
                        {
                            "text": f"Fake response to: {last_message}"
                        }
                    ]
                }
            }
        }