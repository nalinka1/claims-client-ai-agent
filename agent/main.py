import os

from agent.bedrock_model_client import BedrockModelClient
from agent.claims_agent import ClaimsAgent
from knowledge.knowledge_loader import KnowledgeLoader
from knowledge.knowledge_chunker import KnowledgeChunker
from knowledge.knowledge_retriever import KnowledgeRetriever

def main():
    model_client = BedrockModelClient(
            model_id=os.environ["BEDROCK_MODEL_ID"],
            region_name=os.environ["AWS_REGION"],
        )
    # Load approved claims knowledge
    loader = KnowledgeLoader("knowledge/KNOWLEDGE_BASE.md")
    content = loader.load()

    # Divide knowledge into sections
    chunker = KnowledgeChunker()
    chunks = chunker.chunk(content)

    # Create the knowledge retriever
    knowledge_retriever = KnowledgeRetriever(chunks)

    agent = ClaimsAgent(
        model_client=model_client,
        knowledge_retriever=knowledge_retriever)

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