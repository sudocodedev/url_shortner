from django.db import connection

def execute_query(query:str, fetch:bool=False):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            if fetch:
                return cursor.fetchone()
    except Exception:
        return None
