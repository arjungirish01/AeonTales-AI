from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
import os

STORE_PATH = "data/faiss_store"

def build_vector_store(events=None):
    """
    Initialize FAISS vector store. 
    If no events exist, returns None.
    """
    events = events or []

    embeddings = OpenAIEmbeddings()

    if events:
        docs = [Document(page_content=e) for e in events]

        if os.path.exists(STORE_PATH):
            return FAISS.load_local(STORE_PATH, embeddings)
        
        return FAISS.from_documents(docs, embeddings)
    
    return None  # No FAISS yet

def save_vector_store(vectorstore):
    """
    Save FAISS vectorstore if it exists.
    """
    if vectorstore:
        os.makedirs(STORE_PATH, exist_ok=True)
        vectorstore.save_local(STORE_PATH)

def add_event_to_vectorstore(vectorstore, event):
    """
    Add a new story event to FAISS.
    If vectorstore doesn't exist yet, initialize it.
    """
    embeddings = OpenAIEmbeddings()
    doc = Document(page_content=event)

    if vectorstore:
        vectorstore.add_documents([doc])
    else:
        vectorstore = FAISS.from_documents([doc], embeddings)
    
    return vectorstore

