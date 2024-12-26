import streamlit as st
from main import process_query

def app():
    st.title("RAG System")
    user_query = st.text_input("Enter your query:")
    if st.button("Submit"):
        result = process_query(user_query)
        st.write("Answer:", result)
