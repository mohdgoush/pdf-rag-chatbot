import streamlit as st
import time

from src.pdf_reader import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_relevant_chunks
from src.rag_pipeline import generate_response


# PAGE CONFIG
st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
)


# TITLE
st.markdown(
    """
    <h1 style='text-align: center;'>
        📄 AI PDF RAG Chatbot
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# SIDEBAR
with st.sidebar:

    st.header("⚡ About")

    st.write("""
    This chatbot uses:

    - Groq Llama 3.3 70B
    - FAISS Vector Search
    - Sentence Transformers
    - Conversational RAG
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.chat_history = []

        st.success("Chat cleared!")


# SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None


# FILE UPLOAD
uploaded_file = st.file_uploader(
    "📂 Upload your PDF",
    type="pdf"
)


if uploaded_file:

    # Save PDF
    pdf_path = f"data/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # PDF Info
    st.info(f"📘 Uploaded File: {uploaded_file.name}")

    # PROCESS PDF
    with st.spinner("⚙️ Processing PDF..."):

        text = extract_text_from_pdf(pdf_path)

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        vector_store = create_vector_store(embeddings)

        st.session_state.vector_store = vector_store
        st.session_state.chunks = chunks

    st.success("✅ PDF processed successfully!")

    st.markdown("---")


    # DISPLAY CHAT HISTORY
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


    # CHAT INPUT
    query = st.chat_input("💬 Ask a question about the PDF...")


    if query:

        # USER MESSAGE
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": query
            }
        )

        with st.chat_message("user"):
            st.markdown(query)

        # RETRIEVAL
        retrieved_chunks = retrieve_relevant_chunks(
            query,
            model,
            st.session_state.vector_store,
            st.session_state.chunks
        )

        # GENERATE RESPONSE
        response = generate_response(
            query,
            retrieved_chunks,
            st.session_state.chat_history
        )

        # ASSISTANT MESSAGE
        with st.chat_message("assistant"):

            message_placeholder = st.empty()

            full_response = ""

            # TYPING EFFECT
            for word in response.split():

                full_response += word + " "

                time.sleep(0.03)

                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        # SAVE RESPONSE
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )