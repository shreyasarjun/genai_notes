import cohere

def rerank_results(results, query):
    """
    Re-rank search results using Cohere's re-ranking model.
    """
    co = cohere.Client("YOUR_COHERE_API_KEY")
    reranked = co.rerank(
        model="rerank-english-v2.0",
        query=query,
        documents=[result["text"] for result in results]
    )
    return reranked
