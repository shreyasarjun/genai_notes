from config.db_config import get_db_connection

def execute_query(query):
    """Execute SQL query and return results."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as e:
        result = {"error": str(e)}
    finally:
        cursor.close()
        connection.close()
    return result
