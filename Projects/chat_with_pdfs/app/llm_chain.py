import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")

def create_llm_chain(retriever):
    """
    Creates an LLM chain for answering questions using a retriever.
    
    Args:
        retriever (Retriever): The retriever to use for fetching documents relevant to the query.
    
    Returns:
        RetrievalQA: A RetrievalQA chain using the OpenAI LLM.
    """
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=openai_api_key)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return chain
