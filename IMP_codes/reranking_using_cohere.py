import cohere


co = cohere.Client(API_KEY)

def rerank_with_cohere(query, candidates):
    response = co.rerank(
        model='rerank-english-v2.0',
        query=query,
        documents=candidates,
    )

    # Map results back to their original documents using the indices
    reranked_candidates = [
        {
            "document": candidates[result.index],  # Use the index to map back to the original document
            "relevance_score": result.relevance_score,
        }
        for result in response.results
    ]

    # Sort candidates by relevance score in descending order
    reranked_candidates = sorted(
        reranked_candidates,
        key=lambda x: x["relevance_score"],
        reverse=True
    )

    return reranked_candidates

# Test the function
query = "Best machine learning tutorials"
candidates = [
    "AAA is best book of machine learning",
    "Learn machine learning in 10 minutes",
    "Top Python tutorials for beginners",
    "Best resources for deep learning",
    "An introduction to AI and machine learning",
    "I am from India"
]

results = rerank_with_cohere(query, candidates)

print("Reranked Results:")
for item in results:
    print(f"Score: {item['relevance_score']:.2f}, Document: {item['document']}")
