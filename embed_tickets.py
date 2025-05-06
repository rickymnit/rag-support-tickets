import json
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("tickets.json") as f:
    tickets = json.load(f)

texts = [f"{t['title']}. {t['issue']}. {t['resolution']}" for t in tickets]
embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

with open("ticket_data.pkl", "wb") as f:
    pickle.dump((tickets, index, embeddings), f)