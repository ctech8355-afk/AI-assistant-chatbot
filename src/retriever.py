import pickle
import faiss

from sentence_transformers import SentenceTransformer


INDEX_PATH = "vector_store/faiss_index.bin"
METADATA_PATH = "vector_store/metadata.pkl"


model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(INDEX_PATH)

with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)


def retrieve(query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        results.append(metadata[idx])

    return results