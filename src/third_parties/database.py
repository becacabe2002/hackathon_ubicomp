import psycopg2
from psycopg2.extras import RealDictCursor
from src.config import settings

def run_sql_query(query: str) -> list[dict]:
    """
    Execute an SQL query using the PostgreSQL connection string from config,
    and return the result as a list of dictionaries (column names as keys).

    Args:
        query (str): The SQL query to execute.

    Returns:
        list[dict]: The query result as a list of dictionaries.
    """
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(settings.POSTGRES_STRING_URL)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        if cursor.description:  # If the query returns rows
            result = cursor.fetchall()
            return [dict(row) for row in result]
        else:
            conn.commit()  # For INSERT/UPDATE/DELETE
            return []
    except Exception as e:
        # Optionally, log the error here
        raise RuntimeError(f"Database query failed: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
