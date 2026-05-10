# 🌱 Sugarcane Farming Advisory Chatbot using RAG

## 📌 Problem Statement

Farmers often face difficulties in accessing accurate and timely information related to sugarcane farming practices such as cultivation methods, irrigation, fertilizers, pest control, and yield improvement.

This project aims to build an AI-powered advisory chatbot using Retrieval-Augmented Generation (RAG) that can answer farming-related questions by retrieving information from agricultural PDF documents and generating intelligent responses.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- FAISS Vector Database
- Sentence Transformers
- Groq API
- PyPDFLoader
- dotenv

---

# 📂 Project Structure

```plaintext
Sugarcane-Farming-Advisory-Chatbot/
│
├── app/
│   ├── rag_chain.py
│   ├── retriever.py
│
├── data/
│   ├── farming_guide.pdf
│   ├── irrigation_guide.pdf
│
├── vectorstore/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
├── .env
├── README.md
