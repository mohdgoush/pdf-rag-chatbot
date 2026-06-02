from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_relevant_chunks


pdf_path = "data/IET_lucknow_guideline_pdf.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

vector_store = create_vector_store(embeddings)

query = input("Enter your question: ")

retrieved_chunks = retrieve_relevant_chunks(
    query,
    model,
    vector_store,
    chunks
)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(retrieved_chunks):

    print(f"\nChunk {i+1}:\n")

    print(chunk)
    print("-" * 80)