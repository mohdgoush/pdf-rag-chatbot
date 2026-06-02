def chunk_text(pages, chunk_size=500, overlap=100):

    chunked_data = []

    for page in pages:

        source = page["source"]

        page_number = page["page"]

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunked_data.append(
                {
                    "source": source,
                    "page": page_number,
                    "text": chunk
                }
            )

            start += chunk_size - overlap

    return chunked_data
