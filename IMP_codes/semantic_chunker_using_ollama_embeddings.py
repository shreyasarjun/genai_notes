from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import OllamaEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Initialize the embeddings
embeddings = OllamaEmbeddings(model="llama3.2")
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
