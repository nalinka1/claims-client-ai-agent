import re


class KnowledgeRetriever:

    STOP_WORDS = {
        "what", "which", "where", "when", "how",
        "do", "does", "did", "i", "my", "me",
        "the", "a", "an", "is", "are", "for",
        "to", "of", "in", "on", "with", "might",
        "can", "could", "would", "should",
        "claim", "claims", "demo", "services"
    }

    def __init__(self, chunks: list[dict]):
        self.chunks = chunks

    def tokenize(self, text: str) -> set[str]:
        words = set(re.findall(r"\b\w+\b", text.lower()))

        return words - self.STOP_WORDS

    def search(self, query: str) -> list[dict]:
        query_words = self.tokenize(query)
        results = []

        for chunk in self.chunks:

            title_words = self.tokenize(chunk["title"])
            content_words = self.tokenize(chunk["content"])

            score = (
                5 * len(query_words & title_words)
                + len(query_words & content_words)
            )

            if score > 0:
                results.append((score, chunk))

        results.sort(key=lambda item: item[0], reverse=True)

        return [chunk for score, chunk in results]