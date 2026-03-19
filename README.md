# 🚀 RAG + ML + LLM Pipeline

This project implements an end-to-end **AI-powered Retrieval-Augmented Generation (RAG) system** with an added **Machine Learning (ML) prediction layer** to improve response quality and efficiency.

---

## 🧠 Overview

The application combines:

* **RAG UI** for document ingestion and chat interaction
* **Vector Database (ChromaDB)** for storing and retrieving document embeddings
* **ML Model** for predicting query quality before LLM execution
* **LangChain** for orchestrating LLM interactions
* **LLM (via Ollama or API)** for final response generation

---

## 🔄 Workflow

1. **Document Ingestion**

   * Documents are uploaded via RAG UI
   * Text is chunked and stored in **ChromaDB** as embeddings

2. **User Query**

   * User submits a query through the chat UI

3. **Retrieval**

   * Relevant chunks are fetched from ChromaDB

4. **ML Prediction**

   * A lightweight ML model evaluates:

     * Query length
     * Number of retrieved chunks
   * Predicts **response quality score**

5. **Decision Layer**

   * If predicted quality is low → user is prompted to refine query
   * If acceptable → proceed to LLM

6. **LLM Processing**

   * Query + retrieved context sent via **LangChain**
   * LLM generates final response

---

## 🏗️ Architecture

```
RAG UI (Frontend)
        ↓
ChromaDB (Vector Store)
        ↓
Retrieval Layer
        ↓
ML Prediction Layer
        ↓
LangChain Orchestration
        ↓
LLM (Ollama / API)
        ↓
Final Response
```

---

## 🔥 Key Features

* 📄 Document ingestion with chunking
* 🔍 Context-aware retrieval using vector search
* 🧠 ML-based query quality prediction
* 💰 Cost optimization by avoiding low-quality LLM calls
* ⚡ FastAPI-based backend
* 🔗 LangChain integration for LLM workflows

---

## 🎯 Purpose

* Improve **RAG response accuracy**
* Reduce **unnecessary LLM calls (cost optimization)**
* Introduce **intelligence before generation**
* Build a foundation for **AI-driven decision systems**

---

## 🚀 Future Enhancements

* Replace basic ML with advanced models
* Add similarity score as ML feature
* Integrate **MLflow** for experiment tracking
* Deploy on Kubernetes (AKS/EKS)
* Add AI Ops use case (e.g., Kubernetes log analysis)
* This is classic RAG but to convert to agentic AI we need to embeed this using langchain tools 

---

## 👨‍💻 Author

Rupesh Nayak
