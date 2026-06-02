from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_relevant_chunks
from src.rag_pipeline import generate_response


pdf_path = "data/IET_lucknow_guideline_pdf.pdf"

print("\nReading PDF...")

text = extract_text_from_pdf(pdf_path)

print("Chunking text...")

chunks = chunk_text(text)

print("Creating embeddings...")

embeddings = create_embeddings(chunks)

print("Creating vector store...")

vector_store = create_vector_store(embeddings)
chat_history = []

print("\nRAG Chatbot Ready!")

while True:

    query = input("\nAsk a question: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    retrieved_chunks = retrieve_relevant_chunks(
        query,
        model,
        vector_store,
        chunks
    )

    response = generate_response(
        query,
        retrieved_chunks,
        chat_history
    )

    print("\nAnswer:\n")

    print(response)

    # Save user message
    chat_history.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Save assistant response
    chat_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )