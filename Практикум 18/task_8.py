from functools import wraps
from datetime import datetime


def log_exceptions(log_file: str):
    """
    Creates a decorator that logs any exceptions raised by the decorated function.

    When an exception occurs, the decorator writes a log message containing the timestamp,
    exception type, and exception message to the specified log file. The exception is then
    re-raised to preserve the original behavior.

    Args:
        log_file: The path to the log file where exception messages will be appended

    Returns:
        A decorator function that wraps the original function with exception logging functionality
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                exception_type = type(e).__name__
                log_message = f'{current_time} - {exception_type} - {str(e)}'

                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(log_message + '\n')

                raise

        return wrapper

    return decorator



