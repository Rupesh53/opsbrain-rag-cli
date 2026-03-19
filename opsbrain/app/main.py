import os
import time

from opsbrain.config import (
    DATA_DIR,
    CHROMA_DIR,
    LLM_PROVIDER,
    LLM_MODEL
)
from opsbrain.providers.llm import get_llm
from opsbrain.ingestion.loaders import load_documents
from opsbrain.ingestion.splitter import split_documents
from opsbrain.ingestion.indexer import get_or_create_vectorstore, add_documents

from opsbrain.app.rag_chain import create_rag_chain


def main():
    
    print("Return existing chromedb")
    vectorstore = get_or_create_vectorstore()
    
    print("Initiate llm")
    # Create LLM
    llm = get_llm(
        provider=LLM_PROVIDER,
        model=LLM_MODEL
    )
    print(llm)

    # Build RAG chain
    chain = create_rag_chain(vectorstore, llm)

    # Interactive loop
    while True:
        query = input("\nEnter your query (exit/quit to stop): ")

        if query.lower() in {"exit", "quit"}:
            print("👋 Bye!")
            break

        if len(query) > 1000:
            print("❌ Query too long")
            continue

        start = time.time()
        result = chain.invoke({"question": query})
        latency = time.time() - start

        answer = result["answer"]
        sources = result["sources"]

        print(f"\nAnswer:\n{answer}")
        print(f"\n⏱️ Latency: {latency:.2f}s")

        print("\n📚 Sources:")
        seen = set()
        for doc in sources:
            src = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page")
            label = f"{src} (page {page})" if page else src

            if label not in seen:
                print(f"- {label}")
                seen.add(label)
