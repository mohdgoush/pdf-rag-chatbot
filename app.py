from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store


pdf_path = "data/IET_lucknow_guideline_pdf.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

vector_store = create_vector_store(embeddings)

print("FAISS Vector Store Created Successfully!")

print(f"Total vectors stored: {vector_store.ntotal}")