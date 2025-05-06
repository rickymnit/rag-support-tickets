import streamlit as st
from utils import get_top_k
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(query, tickets):
    prompt = f"""You are a support assistant. Use the following tickets to answer the query.

Query: {query}

Tickets:
{[f"Title: {t['title']}, Issue: {t['issue']}, Resolution: {t['resolution']}" for t in tickets]}

Answer:"""
    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response['choices'][0]['message']['content']

st.title("🎫 RAG-Based Support Ticket Helper")

query = st.text_input("Enter support query")

if query:
    with st.spinner("Retrieving relevant tickets..."):
        top_tickets = get_top_k(query, k=2)

        st.subheader("🔍 Relevant Tickets")
        for t in top_tickets:
            st.markdown(f"**Title:** {t['title']}  \n**Issue:** {t['issue']}  \n**Resolution:** {t['resolution']}")

        st.subheader("💡 Suggested Resolution")
        st.write(generate_summary(query, top_tickets))
