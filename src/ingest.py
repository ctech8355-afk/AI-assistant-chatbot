import os
import pickle
import faiss

from sentence_transformers import SentenceTransformer


DOCS_PATH = "docs"
INDEX_PATH = "vector_store/faiss_index.bin"
METADATA_PATH = "vector_store/metadata.pkl"


model = SentenceTransformer("all-MiniLM-L6-v2")


chunks = []
metadata = []


for filename in os.listdir(DOCS_PATH):

    filepath = os.path.join(DOCS_PATH, filename)

    with open(filepath, "r", encoding="utf-8") as file:

        text = file.read()

        paragraphs = text.split("\n\n")

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if paragraph:

                chunks.append(paragraph)

                metadata.append({
                    "source": filename,
                    "text": paragraph
                })


embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, INDEX_PATH)

with open(METADATA_PATH, "wb") as f:
    pickle.dump(metadata, f)

print("Documents indexed successfully.")