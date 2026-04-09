import json
from functools import wraps


def to_json(func):
    """
    Converts the return value of a function to a formatted JSON string.
    The decorator wraps a function and transforms its return value into a JSON string
    with ensure_ascii=False (preserving non-ASCII characters) and 2-space indentation.
    Args:
        func: The function to be decorated

    Returns:
        A wrapper function that returns the JSON string representation of the original function's result
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False, indent=2)

    return wrapper