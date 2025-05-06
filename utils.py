import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pickle

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_ticket_data():
    with open("ticket_data.pkl", "rb") as f:
        return pickle.load(f)

def get_top_k(query, k=2):
    tickets, index, embeddings = load_ticket_data()
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k)
    return [tickets[i] for i in I[0]]