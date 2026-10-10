SEARCH_KNOWLEDGE_BASE_TOOL = {
    "toolSpec": {
        "name": "search_knowledge_base",
        "description": (
            "Search the approved Demo Claims Services knowledge base "
            "for information about claim processes, documents, "
            "claim statuses, enquiries, urgency and privacy. "
            "Use this tool when answering questions that require "
            "official claims information."
        ),
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": (
                            "The claims-related question or search query."
                        )
                    }
                },
                "required": ["query"]
            }
        }
    }
}