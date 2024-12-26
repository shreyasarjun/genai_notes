from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
# Initialize the semantic chunker
chunker = SemanticChunker(
    embeddings=embeddings,
    buffer_size=1,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=0.5  # Adjust based on similarity threshold
)

# Sample text to chunk
text = """
LangChain provides a robust platform for building applications using LLMs. 
It includes tools for text splitting, retrieval, and embeddings, among others. 
Semantic chunking is a powerful method for preprocessing large texts effectively.
My name is shreyas and I am from India.I am name Shreyas and I am from Karnataka.
Semantic chunking provides more effective method.
"""

# Split text into semantic chunks
chunks = chunker.split_text(text)

print(chunks)

# # Print the resulting chunks
# for chunk in chunks:
#     print(chunk)
