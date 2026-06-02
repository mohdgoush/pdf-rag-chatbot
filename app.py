from src.pdf_reader import extract_text_from_pdf
pdf_path = "data/IET_lucknow_guideline_pdf.pdf"
text = extract_text_from_pdf(pdf_path)
print(text[:1000])