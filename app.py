from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings


pdf_path = "data/IET_lucknow_guideline_pdf.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print(f"Total Chunks: {len(chunks)}")

print(f"Embedding Shape: {embeddings.shape}")

print("\nFirst Embedding Vector:\n")

print(embeddings[0])