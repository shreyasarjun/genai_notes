from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os
from app.streamlit_gui import main

if __name__ == "__main__":
    os.makedirs("vector_store", exist_ok=True)
    os.makedirs("pdf_documents", exist_ok=True)
    main()
