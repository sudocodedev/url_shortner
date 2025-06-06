from django.db import connection


def execute_query(query: str, fetch: bool = False):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            if fetch:
                return cursor.fetchone()
    except Exception:
        return None


BASE58_STR_LOOKUP = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def encode_digit(digit: int, base: int = 58) -> str:
    num_str = []
    while digit > 0:
        digit, remainder = divmod(digit, base)
        num_str.append(BASE58_STR_LOOKUP[remainder])
    return "".join(reversed(num_str))
