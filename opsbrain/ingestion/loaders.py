from langchain_community.document_loaders import TextLoader
import os

def load_documents(path):
    docs = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if file.endswith(".txt"):
            loader = TextLoader(full_path)
            docs.extend(loader.load())
    return docs