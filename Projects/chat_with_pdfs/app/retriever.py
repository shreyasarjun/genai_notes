def get_retriever(vector_store, search_type="mmr", k=5):
    """
    Returns a retriever instance from the vector store.
    
    Args:
        vector_store (Chroma): The Chroma vector store to use for retrieval.
        search_type (str): The type of search (e.g., "mmr" for maximum marginal relevance).
        k (int): The number of results to retrieve.
    
    Returns:
        Retriever: A retriever object configured with the specified settings.
    """
    return vector_store.as_retriever(search_type=search_type, search_kwargs={"k": k})
