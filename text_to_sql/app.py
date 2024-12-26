import streamlit as st
from modules.langchain_utils import create_langchain_model
from modules.query_execution import execute_query

st.set_page_config(page_title="Text-to-SQL", layout="wide")
st.title("Text-to-SQL Database Query Tool")

# Initialize LangChain Model
st.sidebar.header("Configuration")
model = create_langchain_model()

# User Input
user_input = st.text_area("Enter your question about the database:", "")

if st.button("Generate SQL"):
    if user_input.strip():
        with st.spinner("Processing..."):
            try:
                # Generate SQL Query
                sql_query = model.run(user_input)
                st.subheader("Generated SQL Query")
                st.code(sql_query)

                # Execute SQL Query
                query_result = execute_query(sql_query)
                st.subheader("Query Result")
                st.write(query_result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid input.")
