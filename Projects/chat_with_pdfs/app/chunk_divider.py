from langchain.text_splitter import RecursiveCharacterTextSplitter

def divide_into_chunks(documents, chunk_size: int = 500, chunk_overlap: int = 50):
    """
    Divides the loaded documents into smaller chunks suitable for embedding.
    
    Args:
        documents (List[Document]): List of LangChain Document objects to be split.
        chunk_size (int): The maximum size of each text chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.
    
    Returns:
        List[str]: A list of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    all_chunks = []
    
    for document in documents:
        chunks = text_splitter.split_text(document.page_content)
        all_chunks.extend(chunks)
    
    return all_chunks
