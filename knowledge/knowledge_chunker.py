class KnowledgeChunker:

    def chunk(self, content: str) -> list[dict]:
        chunks = []
        current_title = None
        current_lines = []

        for line in content.splitlines():

            # Detect a new section heading
            if line.startswith("## "):

                # Save the previous section
                if current_title is not None:
                    chunks.append({
                        "title": current_title,
                        "content": "\n".join(current_lines).strip()
                    })

                # Start a new section
                current_title = line.removeprefix("## ").strip()
                current_lines = []

            elif current_title is not None:
                current_lines.append(line)

        # Save the final section
        if current_title is not None:
            chunks.append({
                "title": current_title,
                "content": "\n".join(current_lines).strip()
            })

        return chunks