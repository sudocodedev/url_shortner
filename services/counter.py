from django.core.exceptions import ValidationError
from common.helpers import execute_query


class CounterService:
    @staticmethod
    def create_counter(name: str):
        query = f"CREATE SEQUENCE IF NOT EXISTS {name} START 1000000000;"
        execute_query(query)

    @staticmethod
    def drop_counter(name: str):
        query = f"DROP SEQUENCE {name};"
        execute_query(query)

    @staticmethod
    def alter_counter(name: str, digit: int):
        query = f"ALTER SEQUENCE {name} RESTART WITH {digit};"
        execute_query(query)

    @staticmethod
    def fetch_value(name: str, type: str):
        operations = {"next": "nextval", "current": "currval"}
        if type not in operations:
            raise ValidationError(f"Invalid type provided.")
        query = f"SELECT {operations[type]}('{name}');"
        result = execute_query(query=query, fetch=True)
        return result[0] if result else None
