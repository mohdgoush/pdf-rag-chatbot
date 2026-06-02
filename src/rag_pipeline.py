from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(query, retrieved_chunks, chat_history):

    context = ""

    for chunk in retrieved_chunks:

        context += f"""
    Page Number: {chunk['page']}

    Content:
    {chunk['text']}

    """

    history = ""

    for message in chat_history:

        role = message["role"]
        content = message["content"]

        history += f"{role}: {content}\n"

    prompt = f"""
You are a helpful AI assistant.

Use the provided context and conversation history
to answer the user's question.

Conversation History:
{history}

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,
        max_tokens=1024
    )

    return response.choices[0].message.content