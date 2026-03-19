def format_docs(docs):
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        formatted.append(f"[{i}] ({source}) {doc.page_content}")
    return "\n\n".join(formatted)


def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "lambda_mult": 0.7}
    )

def retrieve_chunk_text(text, chunk_size=200, overlap=50):
    chunks = []
    
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        start += chunk_size - overlap  # overlap for context
    
    return chunks