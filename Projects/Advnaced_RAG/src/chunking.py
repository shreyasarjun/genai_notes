import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings  # Updated import
from langchain_experimental.text_splitter import SemanticChunker

# Load environment variables from the sibling .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Initialize OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI embeddings with your API key
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)

# Initialize the semantic chunker
chunker = SemanticChunker(
    embeddings=embeddings,
    buffer_size=1,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=0.5  # Adjust based on similarity threshold
)

def perform_semantic_chunking(input_text: str):
    """
    Accepts text as input and performs semantic chunking.

    Args:
        input_text (str): The text to be chunked.
        
    Returns:
        list: A list of semantic chunks.
    """
    # Split text into semantic chunks
    chunks = chunker.split_text(input_text)
    return chunks

# Example usage:
# out=perform_semantic_chunking('This is India, This is karnataka')
# print(out)
