import os
#from langchain.chains import SQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain
#from langchain.chains.sql_database.base import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def create_langchain_model():
    """Initialize LangChain SQLDatabaseChain with OpenAI."""
    db = SQLDatabase.from_uri(
        f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    return db_chain
