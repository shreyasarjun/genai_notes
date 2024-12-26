import os
from langchain_community.retrievers import BM25Retriever
from langchain.schema import Document
from src.data_loader import load_pdfs
from src.chunking import perform_semantic_chunking
from src.embedding import generate_dense_embeddings, generate_sparse_embeddings, save_embeddings
# from src.query_translation import query_rewriting, generate_multi_queries
# from src.hybrid_search import perform_hybrid_search
# from src.re_ranker import rerank_results
# from src.answer_generator import generate_final_answer

# Define paths
PDF_FOLDER = "./data/pdfs"
EMBEDDING_FOLDER = "./data/embeddings"

def main():
    # Step 1: Load PDFs and extract text
    print("Loading and extracting text from PDFs...")
    pdf_texts = load_pdfs(PDF_FOLDER)
    print(type(pdf_texts))
    print(pdf_texts)
    
    # Step 2: Semantic Chunking
    print("Performing semantic chunking...")
    all_chunks = []
    for file_name, text in pdf_texts.items():
        chunks = perform_semantic_chunking(text)
        print("333333333333333")
        all_chunks.extend(chunks)

    print(type(all_chunks))
    print(all_chunks)

    documents = [Document(page_content=chunk) for chunk in chunks]
    
    # Step 3: Generate embeddings (dense and sparse)
    print("Generating dense and sparse embeddings...")
    os.makedirs(EMBEDDING_FOLDER, exist_ok=True)
    #dense_vectors = generate_dense_embeddings(documents,EMBEDDING_FOLDER)
    sparse_vectors = generate_sparse_embeddings(documents)
    
    # Save embeddings
    save_embeddings(sparse_vectors, EMBEDDING_FOLDER)
    
    # # Wait for user query
    # print("\n--- System Ready ---")
    # user_query = input("Enter your query: ")
    
    # # Step 4: Query Translation
    # print("Translating query...")
    # rewritten_query = query_rewriting(user_query)
    # multi_queries = generate_multi_queries(rewritten_query)
    
    # # Step 5: Hybrid Search
    # print("Performing hybrid search...")
    # query_vector = dense_vectors[0]  # Example: use the first dense vector as a placeholder
    # results = perform_hybrid_search(dense_vectors, sparse_vectors, query_vector)
    
    # # Step 6: Re-Ranking
    # print("Re-ranking results...")
    # reranked_results = rerank_results(results, user_query)
    
    # # Step 7: Generate Final Answer
    # print("Generating final answer...")
    # top_context = reranked_results[0]["text"]  # Use the top result's text
    # final_answer = generate_final_answer(user_query, top_context)
    
    # print("\n--- Final Answer ---")
    # print(final_answer)

if __name__ == "__main__":
    main()
