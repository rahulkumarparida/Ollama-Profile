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



## Outputs
---

<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_37_05" src="https://github.com/user-attachments/assets/d3fcbe97-82f5-4423-9d8e-bf6e9e0c198c" />  
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_30_58" src="https://github.com/user-attachments/assets/3e7235f7-8c18-4c45-a8da-03189f74f65d" />
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 13-11-2025 17_01_47" src="https://github.com/user-attachments/assets/357a9d90-e4cd-47db-8407-d108d94eb60e" />
<img width="1920" height="1020" alt="qa_local py - persolan_model - Visual Studio Code 14-11-2025 15_34_15" src="https://github.com/user-attachments/assets/03a0dff0-0159-40ac-bfc1-748f717aa584" />
