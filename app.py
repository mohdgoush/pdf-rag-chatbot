from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text

pdf_path = "data/IET_lucknow_guideline_pdf.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(text)
print(f"Total Chunks: {len(chunks)}")
print("\nFIRST CHUNK:\n")
print(chunks[0])