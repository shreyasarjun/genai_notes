import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    """Establish a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
    return connection
