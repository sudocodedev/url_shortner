from django.core.exceptions import ValidationError

from common.helpers import execute_query


class CounterService:
    """A simple counter service using DB sequence."""

    @staticmethod
    def create_counter(name: str):
        """
        Creates a PostgreSQL sequence if it doesn't already exist.

        Args:
            name (str): Name of the sequence to create.
        """
        query = f"CREATE SEQUENCE IF NOT EXISTS {name} START 1000000000;"
        execute_query(query)

    @staticmethod
    def drop_counter(name: str):
        """
        Drops an existing PostgreSQL sequence.

        Args:
            name (str): Name of the sequence to drop.
        """
        query = f"DROP SEQUENCE {name};"
        execute_query(query)

    @staticmethod
    def alter_counter(name: str, digit: int):
        """
        Resets the starting value of an existing sequence.

        Args:
            name (str): Name of the sequence.
            digit (int): New starting value for the sequence.
        """
        query = f"ALTER SEQUENCE {name} RESTART WITH {digit};"
        execute_query(query)

    @staticmethod
    def fetch_value(name: str, type: str):
        """
        Fetches a value from a sequence (either next or current).

        Args:
            name (str): Name of the sequence.
            type (str): Type of fetch - "next" for nextval or "current" for currval.

        Returns:
            int or None: The value from the sequence, or None if query fails.

        Raises:
            ValidationError: If the 'type' is not "next" or "current".
        """
        operations = {"next": "nextval", "current": "currval"}
        if type not in operations:
            raise ValidationError("Invalid type provided.")
        query = f"SELECT {operations[type]}('{name}');"
        result = execute_query(query=query, fetch=True)
        return result[0] if result else None
