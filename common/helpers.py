from django.db import connection


def execute_query(query: str, fetch: bool = False):
    """
    Executes a raw SQL query using the default database connection.

    Args:
        query (str): SQL query string to be executed.
        fetch (bool): If True, returns the first row of the result.

    Returns:
        The first row of the query result if fetch is True.
        None if fetch is False or if an exception occurs.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            if fetch:
                return cursor.fetchone()
    except Exception:
        return None

# Lookup
BASE58_STR_LOOKUP = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def encode_digit(digit: int, base: int = 58) -> str:
    """
    Converts an integer to a base-N string using a custom character set (default: Base58).

    Args:
        digit (int): The integer to encode.
        base (int): The numerical base to use (default is 58).

    Returns:
        str: The encoded string representation of the input digit.
    """
    num_str = []
    while digit > 0:
        digit, remainder = divmod(digit, base)
        num_str.append(BASE58_STR_LOOKUP[remainder])
    return "".join(reversed(num_str))
