import os
from langchain.document_loaders import PyPDFLoader

def load_pdfs(pdf_dir: str):
    """
    Loads PDF documents from the specified directory using LangChain's PyPDFLoader.
    
    Args:
        pdf_dir (str): Directory containing PDF files.
    
    Returns:
        List[Document]: A list of LangChain Document objects.
    """
    all_documents = []
    
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()  # Loads PDF into LangChain Document objects
            all_documents.extend(documents)
    
    return all_documents
