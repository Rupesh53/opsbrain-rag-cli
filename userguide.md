# 📘 Opsbrain User Guide

This guide helps you install and use cli locally.

---

## 🖥️ Requirements

- Python 3.10+
- pip
- (Optional) Ollama for local models

---

## 📦 Installation

### Clone Repository

```
git clone https://github.com/yourusername/opsbrain-rag-cli.git
cd opsbrain-rag-cli
```
## Install in Editable Mode

```
pip install -e .
```

## 🤖 LLM Setup
### Option 1: Local (Ollama)
```
Install Ollama: https://ollama.com
```
Pull a model:
```
ollama pull dolphin-mistral
```

```
### Option 2: Gemini (Cloud)  if you use :)

Get an API key from Google AI Studio

Install dependency:
```
pip install langchain-google-genai
```

Configure .env:
```
LLM_PROVIDER=gemini
LLM_MODEL=gemini-1.5-pro
GEMINI_API_KEY=your_key_here
```
## 📂 Ingest Documents
```
python -m opsbrain.cli ingest  or 
python -c "from opsbrain.cli import ingest; ingest('./data')"
```
Reset Vector Database
```
opsbrain ingest ./data --reset  or  if typer doesnt work
python -m opsbrain.cli ingest --reset 
python -c "from opsbrain.cli import ingest; ingest('./data')"


```

## Supported formats:

- PDF

- DOCX

- TXT

## 💬 Chat with Your Data
```
python -m opsbrain.cli chat  or 
python -c "from opsbrain.cli import chat; chat()"
```

Exit with:
```
exit
quit
```

```
## 🧠 Best Practices

- Use clean, text-based PDFs

- Avoid scanned documents

- Reset DB after major document changes

- Keep documents topic-focused

## 🛠️ Troubleshooting
LLM not responding

- Ensure Ollama is running

- Check API keys

Empty answers

- Documents not ingested

- Retriever k too low

- Question outside document scope
