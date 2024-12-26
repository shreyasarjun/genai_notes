# import pandas as pd
# import streamlit as st
# from operator import itemgetter
# from pydantic import BaseModel, Field
# from typing import List
# from langchain.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain.schema import BaseOutputParser

# # Initialize the Chat Model
# llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0)

# # Cache the function to read table details
# @st.cache_data
# def get_table_details():
#     # Read the CSV file into a DataFrame
#     table_description = pd.read_csv("database_table_descriptions.csv")
#     table_docs = []

#     # Iterate over the DataFrame rows to create Document objects
#     table_details = ""
#     for index, row in table_description.iterrows():
#         table_details += f"Table Name: {row['Table']}\nTable Description: {row['Description']}\n\n"

#     return table_details

# # Define the schema using a Pydantic model
# class Table(BaseModel):
#     """Table in SQL database."""
#     name: str = Field(description="Name of table in SQL database.")

# # Function to extract table names from the structured output
# def get_tables(tables: List[Table]) -> List[str]:
#     return [table.name for table in tables]

# # Retrieve table details
# table_details = get_table_details()

# # Define the prompt for the LLM
# table_details_prompt = ChatPromptTemplate.from_template(
#     template=(
#         "System Message: Return the names of ALL the SQL tables that MIGHT be relevant to the user question. "
#         "The tables are:\n\n"
#         f"{table_details}\n\n"
#         "Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.\n\n"
#         "Human Message: Question: {question}"
#     )
# )

# # Use `with_structured_output` to replace `create_extraction_chain_pydantic`
# llm_chain = llm.with_structured_output(schema=Table)

# # Updated chain
# def table_chain(question: str) -> List[str]:
#     # Extract the relevant tables based on the question
#     structured_output = llm_chain.run(question)
#     return get_tables(structured_output)

# # Example usage in Streamlit
# question = st.text_input("Enter your SQL-related question:")
# if st.button("Get Relevant Tables"):
#     try:
#         relevant_tables = table_chain(question)
#         st.write("Relevant Tables:", relevant_tables)
#     except Exception as e:
#         st.error(f"Error: {e}")


import pandas as pd
import streamlit as st
from operator import itemgetter
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
from typing import List

@st.cache_data
def get_table_details():
    # Read the CSV file into a DataFrame
    table_description = pd.read_csv("database_table_descriptions.csv")
    table_docs = []

    # Iterate over the DataFrame rows to create Document objects
    table_details = ""
    for index, row in table_description.iterrows():
        table_details = table_details + "Table Name:" + row['Table'] + "\n" + "Table Description:" + row['Description'] + "\n\n"

    return table_details


class Table(BaseModel):
    """Table in SQL database."""

    name: str = Field(description="Name of table in SQL database.")

def get_tables(tables: List[Table]) -> List[str]:
    tables  = [table.name for table in tables]
    return tables


# table_names = "\n".join(db.get_usable_table_names())
table_details = get_table_details()
table_details_prompt = f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \
The tables are:

{table_details}

Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""

table_chain = {"input": itemgetter("question")} | create_extraction_chain_pydantic(Table, llm, system_message=table_details_prompt) | get_tables