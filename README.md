# Ollama-Profile (RAG-based Personal Knowledge Assistant)

Ollama-Profile is a **Retrieval-Augmented Generation (RAG)** system built to answer questions **about me** using structured personal data instead of hallucinated responses.

The system uses:
- **JSON-based personal knowledge**
- **Vector embeddings stored in ChromaDB**
- **Local LLM inference using Ollama (Phi-3)**
- **Keyword-based routing for targeted retrieval**

This ensures responses are **context-aware, fast, and accurate**.

---

## 🚀 Features

- 📄 **Structured Personal Knowledge Base**
  - Personal data stored as JSON (projects, skills, education, achievements, etc.)

- 🧠 **Vector Search with ChromaDB**
  - Data is chunked, embedded, and stored for semantic retrieval

- 🔀 **Query Routing Logic**
  - Keyword-based routing restricts retrieval to relevant chunks  
  - Example: project-related queries search only project vectors

- 🤖 **Local LLM via Ollama**
  - Uses `phi3` model for lightweight, fast inference
  - No cloud APIs, fully local execution

- ❌ **No Hallucinations**
  - Model answers strictly from retrieved context
  - If data doesn’t exist, it says so

---

## 🧩 Architecture Overview

```text
User Query
   ↓
Keyword Router
   ↓
Relevant Vector Collection (ChromaDB)
   ↓
Context Retrieval
   ↓
Ollama (Phi-3)
   ↓
Final Answer
```

```text
Ollama-Profile/
│
├── data/
│   └── profile.json        # Structured personal data
│
├── vector_store/
│   └── chroma/             # ChromaDB persistent storage
│
├── embedding.py            # Chunking & vectorization logic
├── retriever.py            # Context retrieval + routing
├── llm.py                  # Ollama model interface
├── main.py                 # Entry point
│
├── requirements.txt
└── README.md
```

## ⚙️ Tech Stack
```text
Python

Ollama

Phi-3 LLM

ChromaDB

Sentence Transformers / Embeddings

JSON-based knowledge representation
```

## ▶️ How It Works
```text
Personal data is written in structured JSON format

Data is chunked and converted into embeddings

Embeddings are stored in ChromaDB

User query is analyzed using keyword routing

Only relevant chunks are retrieved

Ollama’s Phi-3 generates answers using retrieved context

```
## 🛠️ Installation & Setup
```bash
# Clone the repo
git clone https://github.com/rahulkumarparida/Ollama-Profile.git
cd Ollama-Profile

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull Phi-3 model
ollama pull phi3

# Run the app
python main.py

```

```text
📌 Example Queries

“What projects has he built?”

“What technologies does he know?”

“Tell me about his education”

“What are his achievements?”

Each query retrieves only the relevant vector space, not the entire dataset.

```

## 🎯 Why This Project Matters

```text
Demonstrates real RAG implementation, not just API calls

Shows understanding of:

Embeddings

Vector databases

Context grounding

Query routing

Fully local, privacy-preserving AI system

```


## Outputs
---

<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_37_05" src="https://github.com/user-attachments/assets/d3fcbe97-82f5-4423-9d8e-bf6e9e0c198c" />  
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_30_58" src="https://github.com/user-attachments/assets/3e7235f7-8c18-4c45-a8da-03189f74f65d" />
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 13-11-2025 17_01_47" src="https://github.com/user-attachments/assets/357a9d90-e4cd-47db-8407-d108d94eb60e" />
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_34_15" src="https://github.com/user-attachments/assets/03a0dff0-0159-40ac-bfc1-748f717aa584" />


# 📜 License
## MIT License

---

## 🌐 GitHub Pages – About Section (Short & Clean)

Use this for **GitHub Pages / repo About section**:

> **Ollama-Profile** is a Retrieval-Augmented Generation (RAG) system that answers questions about me using structured personal data. It combines ChromaDB for vector search, keyword-based query routing, and a local Phi-3 model via Ollama to deliver accurate, hallucination-free responses — fully offline and privacy-focused.

---

## 🧠 Honest Evaluation (No Hype)

What you did **right**:
- ✅ Real RAG (not prompt stuffing)
- ✅ Vector store separation
- ✅ Routing logic (this is advanced)
- ✅ Local inference (industry-relevant)

What you can add later (optional):
- Metadata-based filtering instead of keyword-only routing
- Hybrid search (BM25 + vector)
- Simple FastAPI wrapper
- UI (Streamlit / React)

If you want, next I can:
- 🔧 Review your **actual code line-by-line**
- 📈 Suggest **resume-ready bullet points**
- 🧪 Help convert this into an **API or SaaS-style project**

Just tell me.

