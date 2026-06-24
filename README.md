# QTrade Support Knowledge Assistant

A lightweight document retrieval and answer generation system for customer support. This repository builds a searchable knowledge base from internal support documents, then uses a local LLM via Ollama to generate grounded answers and identify questions that should be escalated.

## Key Features

- Ingests text documents from `docs/`
- Builds semantic embeddings with `sentence-transformers`
- Stores a FAISS vector index in `vector_store/`
- Retrieves the most relevant passages for a query
- Generates answers with `ollama` and a conversational model
- Performs simple escalation checks for safety-sensitive queries

## Repository Structure

- `docs/` - support content files such as `returns.txt`, `shipping.txt`, `smarthub.txt`, `warranty.txt`
- `vector_store/` - generated FAISS index and metadata storage
- `requirements.txt` - Python dependencies
- `src/`
  - `ingest.py` - build and store the embedding index from documentation
  - `retriever.py` - load the index and retrieve top documents for a query
  - `generator.py` - call Ollama to answer questions using retrieved context
  - `escalation.py` - evaluate whether a query should be escalated
  - `main.py` - orchestration example for the end-to-end flow

## Requirements

- Python 3.10+ (recommended)
- `pip install -r requirements.txt`
- Ollama must be installed and configured if using the answer generation pipeline

## Setup

1. Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Confirm the support document files exist in `docs/`.

## Usage

### 1. Ingest Documents

Build the FAISS index and metadata from the text files in `docs/`:

```powershell
python src\ingest.py
```

This generates:

- `vector_store/faiss_index.bin`
- `vector_store/metadata.pkl`

### 2. Retrieve Relevant Content

Use `src/retriever.py` to fetch the most relevant support passages for a query.

### 3. Generate Answers

Use `src/generator.py` to generate a grounded response from the retrieved context.

### Example Query Flow

```powershell
python - <<'PY'
from src.retriever import retrieve
from src.generator import generate_answer

query = "How do I return a product?"
retrieved = retrieve(query, top_k=3)
answer = generate_answer(query, retrieved)
print(answer)
PY
```

### 4. Escalation Check

`src/escalation.py` exposes a simple function to flag queries containing sensitive keywords:

```python
from src.escalation import should_escalate

if should_escalate("There is smoke coming from my heater"):
    print("Escalate this request")
```

## Notes

- The `src/main.py` file illustrates a full end-to-end pipeline concept, but the repository currently relies on the main support scripts in `src/`.
- The retrieval and answer generation pipeline assumes the index has been built before running queries.
- Update the model name in `src/generator.py` if you want to use a different Ollama model.

## License

Use and modify this project for internal support automation and knowledge retrieval workflows.
