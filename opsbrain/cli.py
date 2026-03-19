import typer
from opsbrain.app.main import main as chat_main
from opsbrain.ingestion.loaders import load_documents
from opsbrain.ingestion.splitter import split_documents
from opsbrain.ingestion.indexer import get_or_create_vectorstore, add_documents
from opsbrain.config import DATA_DIR

app = typer.Typer()

@app.command()
def ingest(data_path: str = DATA_DIR):
    print("🔥 INGEST FUNCTION STARTED")   # <-- ADD THIS

    docs = load_documents(data_path)
    print(f"Loaded {len(docs)} docs")

    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    vectorstore = get_or_create_vectorstore()
    add_documents(vectorstore, chunks)

    print("✅ Ingestion complete")

@app.command()
def chat():
    chat_main()

def run():
    app()