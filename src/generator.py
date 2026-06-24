import ollama


def generate_answer(query, retrieved_docs):

    context = "\n\n".join(
        [
            f"Source: {doc['source']}\n{doc['text']}"
            for doc in retrieved_docs
        ]
    )

    prompt = f"""
Answer ONLY using the provided context.

If the answer is not found, say:
"I don't know based on the provided documentation."

Context:
{context}

Question:
{query}

Include citations.
"""

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]