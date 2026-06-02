import numpy as np


def retrieve_relevant_chunks(query, embedding_model, index, chunks, k=3):

    query_embedding = embedding_model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = []

    for idx in indices[0]:

        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks