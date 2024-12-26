from langchain.llms import OpenAI

def generate_final_answer(query, context):
    """
    Generate final answers using GPT-4.
    """
    llm = OpenAI(model="gpt-4")
    answer = llm.predict(f"Given the context:\n{context}\nAnswer the query: {query}")
    return answer
