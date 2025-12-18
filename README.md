# 🧠 AI Text & PDF Summarizer

An AI-powered web application that summarizes **long text and PDF documents** into **clear, point-wise summaries** using **Transformer-based NLP models**.  
The application ensures **full content coverage** through **chunk-based hierarchical summarization** and provides an **interactive, animated UI** built with Streamlit.

---

## 🚀 Features

- 📄 Upload and summarize **PDF documents**
- ✍️ Paste and summarize **raw text**
- 🧩 **Chunk-based summarization** for full coverage of long documents
- 📌 **Point-wise structured summaries**
- 🎨 Attractive, animated user interface
- 🆓 Uses **free Hugging Face Transformer models**
- 🔐 No API keys or billing required

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **NLP Model:** Hugging Face Transformers  
- **Summarization Model:** `facebook/bart-large-cnn`  
- **PDF Processing:** PyPDF2  

---

## 🧠 How It Works

1. User provides input as **text or PDF**
2. Large input is split into smaller **chunks**
3. Each chunk is summarized individually using a Transformer model
4. All summaries are combined into a **full, point-wise summary**
5. Output is displayed in a **clean and readable format**

This approach avoids information loss in long documents and ensures better coverage.

---

## 📂 Project Structure

ai-text-pdf-summarizer/
│
├── app.py # Main Streamlit application
├── .gitignore # Ignored files (venv, env, cache)
└── README.md # Project documentation


