import streamlit as st

from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_relevant_chunks
from src.rag_pipeline import generate_response


st.set_page_config(
    page_title="PDF RAG Chatbot",
    layout="wide"
)

st.title("📄 PDF RAG Chatbot")


uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)


if uploaded_file:

    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    pdf_path = f"data/{uploaded_file.name}"

    with st.spinner("Processing PDF..."):

        text = extract_text_from_pdf(pdf_path)

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        vector_store = create_vector_store(embeddings)

    st.success("PDF processed successfully!")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    query = st.chat_input("Ask a question about the PDF")

    if query:

        retrieved_chunks = retrieve_relevant_chunks(
            query,
            model,
            vector_store,
            chunks
        )

        response = generate_response(
            query,
            retrieved_chunks,
            st.session_state.chat_history
        )

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": query
            }
        )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    # Display chat history
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.write(message["content"])