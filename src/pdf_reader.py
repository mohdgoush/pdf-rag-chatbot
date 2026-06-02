from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path, filename):

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            pages.append(
                {
                    "source": filename,
                    "page": page_number + 1,
                    "text": text
                }
            )

    return pages
