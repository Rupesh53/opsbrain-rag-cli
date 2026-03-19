from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
from opsbrain.config import CHROMA_DIR

def get_or_create_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    os.makedirs(CHROMA_DIR, exist_ok=True)

    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

def add_documents(vectorstore, chunks):
    if not chunks:
        print("No chunks to add")
        return

    print(f"Adding {len(chunks)} chunks")

    vectorstore.add_documents(chunks)