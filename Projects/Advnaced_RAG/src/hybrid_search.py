from langchain.chains import EnsembleRetriever

def perform_hybrid_search(dense_vectors, sparse_vectors, query_vector):
    """
    Use EnsembleRetriever for hybrid searching.
    """
    ensemble_retriever = EnsembleRetriever(
        retrievers=[dense_vectors, sparse_vectors],
        weights=[0.5, 0.5]
    )
    return ensemble_retriever.retrieve(query_vector)
