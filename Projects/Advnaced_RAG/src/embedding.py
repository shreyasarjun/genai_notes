import os
import json
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Fetch OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")


def generate_dense_embeddings(chunks, persist_directory):
    """
    Generate dense embeddings using OpenAI and store them in Chroma.
    """
    # Initialize OpenAI embeddings with the fetched API key
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    

    # Create Chroma vector store from the documents
    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory)
    
    # Persist the vector store for later use
    vector_store.persist()

    return vector_store

def generate_sparse_embeddings(chunks):
    """
    Generate sparse embeddings using BM25Retriever.
    """
    # Initialize BM25Retriever with the provided chunks
    retriever = BM25Retriever.from_documents(chunks)

    print("88888888888888")
    print(type(retriever))
    print(retriever)

    
    return retriever

def save_embeddings(retriever, output_path):
    """
    Save dense and sparse embeddings to files.
    """
    # # Save dense embeddings (Chroma vector store)
    # dense_embeddings = dense_vector_store.get_all_vectors()
    # with open(f"{output_path}/dense.json", 'w') as f:
    #     json.dump(dense_embeddings, f)

    # For sparse embeddings, we'll use the BM25 retriever to store some basic document info
    try:
        # Attempt to use the to_json method
        json_data = retriever.to_json()
    except AttributeError:
        # Fallback to model_dump_json if to_json is not available
        json_data = retriever.model_dump_json()

    # Convert dictionary to JSON string and write to file
    with open(output_path+'/bm_25_retriver.json', 'w') as f:
        json.dump(json_data, f, indent=4)
