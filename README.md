# RAG-Based Support Ticket System

This is a prototype system that demonstrates **Retrieval-Augmented Generation (RAG)** for customer support. It semantically understands support queries, retrieves the most relevant past tickets using vector search (FAISS), and generates a contextual response using OpenAI's GPT models.

---

## Features

- Semantic retrieval using SentenceTransformers and FAISS
- Sample ticket database (JSON format)
- GPT-generated contextual support response
- 🖥Streamlit-based web interface
- Optional feedback mechanism (can be extended)

---

## Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS (CPU)](https://github.com/facebookresearch/faiss)
- [OpenAI API](https://platform.openai.com/)
- `pipx` and `venv` for clean environment management

---

## ⚙️ Setup (Tested on Ubuntu)

### Step 1: System Preparation

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```
```bash
pipx install --python python3.10 virtualenv
cd ~/Projects/rag-support-tickets
python3.10 -m venv .venv
source .venv/bin/activate
```
```bash
pip install -r requirements.txt
pip install streamlit sentence-transformers faiss-cpu openai
```
```bash
python embed_tickets.py
streamlit run app.py
```
