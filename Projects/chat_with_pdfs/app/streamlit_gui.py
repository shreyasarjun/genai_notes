import streamlit as st
from app.data_loader import load_pdfs
from app.chunk_divider import divide_into_chunks
from app.vector_store import create_vector_store, load_vector_store
from app.retriever import get_retriever
from app.llm_chain import create_llm_chain

PERSIST_DIR = "vector_store/"
PDF_DIR = "pdf_documents/"

def main():
    st.set_page_config(page_title="RAG App", page_icon="📘", layout="wide")
    
    st.markdown("""
        <style>
        .main { background-color: #f9f9f9; }
        </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.image("assets/logo.png", use_container_width=True)  # Updated for deprecation warning
    st.sidebar.title("RAG Configuration")
    
    option = st.sidebar.radio("Options", ["Process PDFs", "Ask Questions"])
    
    if option == "Process PDFs":
        with st.spinner("Processing documents..."):
            documents = load_pdfs(PDF_DIR)
            text_chunks = divide_into_chunks(documents)
            create_vector_store(documents, PERSIST_DIR)
        st.success("PDFs processed and vector store updated!")
    
    elif option == "Ask Questions":
        query = st.text_input("Enter your query:")
        if query:
            vector_store = load_vector_store(PERSIST_DIR)
            retriever = get_retriever(vector_store)
            llm_chain = create_llm_chain(retriever)
            
            with st.spinner("Fetching answer..."):
                # Use chain() instead of run()
                result = llm_chain({"query": query})
            
            # Display the answer
            st.write("**Answer:**", result["result"])
            
            # Display source documents
            with st.expander("Sources"):
                for doc in result["source_documents"]:
                    st.write(f"Source: {doc.metadata.get('source', 'Unknown')}")

if __name__ == "__main__":
    main()
