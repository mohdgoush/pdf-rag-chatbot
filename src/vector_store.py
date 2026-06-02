import faiss
import numpy as np

def create_vector_store(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    embeddings = np.array(embeddings).astype("float32")

    index.add(embeddings)

    return index