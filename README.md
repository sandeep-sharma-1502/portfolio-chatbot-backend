# 🤖 Portfolio AI Chatbot (RAG-based)

🚀 Live Demo: Coming Soon

An AI-powered **Portfolio Chatbot** built using **FastAPI, LangChain, FAISS, HuggingFace Embeddings, and Groq LLM**.

This chatbot works as a **personal portfolio assistant for Sandeep Sharma**, answering **only professional questions** about his skills, experience, projects, and background using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 🤖 Personal AI assistant for **Sandeep Sharma’s portfolio**
- 📄 Understands professional background from structured portfolio data (PDF)
- 🔍 Semantic search using **FAISS vector database**
- 🧠 Free & local embeddings with **HuggingFace Sentence-Transformers**
- ⚡ Ultra-fast LLM inference using **Groq (LLaMA 3.1)**
- 🛑 Prevents off-topic and hallucinated answers
- 🌐 Clean REST API built with **FastAPI**
- 📦 Production-ready backend architecture

---

## 🏗️ Architecture Overview

```
User Question
      ↓
FastAPI (/chat)
      ↓
FAISS Semantic Search
      ↓
Relevant Portfolio Context
      ↓
Groq LLM (llama-3.1-8b-instant)
      ↓
Portfolio-aware Answer
```

---

## 🧰 Tech Stack

### Backend
- FastAPI
- Python 3.11
- Uvicorn

### AI / RAG
- LangChain
- FAISS
- HuggingFace Sentence-Transformers
- Groq LLM (llama-3.1-8b-instant)

### Utilities
- PyMuPDF (PDF parsing)
- python-dotenv
- CORS Middleware

---

## 📂 Project Structure

```
portfolio-chatbot-backend/
│
├── app/
│   ├── main.py              # FastAPI app entry
│   ├── api/
│   │   └── chat.py          # /chat API route
│   ├── services/
│   │   ├── pdf_loader.py    # Portfolio PDF loader
│   │   ├── vector_store.py  # FAISS + embeddings
│   │   └── rag_chain.py     # RAG + Groq logic
│
├── data/
│   └── sandeep_sharma.pdf   # Portfolio / Resume data
│
├── .env                     # Environment variables
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sandeep-sharma-1502/portfolio-chatbot-backend.git
cd portfolio-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

- API Root: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`

---

## 🧪 API Usage Examples

### ✅ Portfolio Question

**Request**
```json
{
  "message": "What skills does Sandeep Sharma have?"
}
```

**Response**
```json
{
  "reply": "Sandeep Sharma has experience in React.js, JavaScript, Tailwind CSS, PHP, and building scalable web applications."
}
```

---

### ❌ Off-topic Question

**Request**
```json
{
  "message": "5 mango names"
}
```

**Response**
```json
{
  "reply": "I can help with questions related to Sandeep Sharma’s professional background, skills, or experience."
}
```

---

## 🧠 Design Decisions

- Used **RAG instead of fine-tuning** for accuracy and control
- Portfolio-restricted answers to avoid hallucination
- FAISS for fast semantic retrieval
- Groq for low-latency inference
- Cached vector store for better performance

---

## 🔐 Security & Best Practices

- API keys managed via environment variables
- Portfolio data never exposed directly
- Clean separation of concerns
- Production-safe logging and configuration

---

## 🌍 Deployment Ready

This backend can be deployed on:
- Render
- Railway
- VPS / Cloud VM

Requirements:
- Python runtime
- GROQ_API_KEY environment variable

---

## 👨‍💻 About the Developer

**Sandeep Sharma**  
Frontend-focused developer with experience in **React, JavaScript, PHP**, and a strong interest in **AI-powered portfolio systems and RAG applications**.

This project demonstrates:
- Real-world AI integration
- Backend architecture skills
- Production-ready engineering mindset

---

## ⭐ Why This Project Stands Out

This is not a generic chatbot — it is a **domain-restricted, portfolio-aware AI assistant** built using real-world RAG architecture patterns.
