import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")

def create_vector_store(documents, persist_directory: str):
    """
    Creates and persists a vector store from the documents using Chroma.
    
    Args:
        documents (List[Document]): List of documents to be converted into vectors.
        persist_directory (str): Directory where the vector store will be saved.
    
    Returns:
        Chroma: The created vector store.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_store = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
    vector_store.persist()
    return vector_store

def load_vector_store(persist_directory: str):
    """
    Loads an existing vector store from the specified directory.
    
    Args:
        persist_directory (str): The directory where the vector store is stored.
    
    Returns:
        Chroma: The loaded vector store.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
