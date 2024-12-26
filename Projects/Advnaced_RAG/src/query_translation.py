from langchain.llms import OpenAI

def query_rewriting(query):
    """
    Perform query rewriting using OpenAI.
    """
    llm = OpenAI(model="gpt-4")
    rewritten_query = llm.predict(f"Rewrite this query for better retrieval: {query}")
    return rewritten_query

def generate_multi_queries(query):
    """
    Generate multiple query variations.
    """
    llm = OpenAI(model="gpt-4")
    multi_queries = llm.predict(f"Generate 3 variations of this query: {query}")
    return multi_queries.split('\n')
