def decorator(func):
    """
    Creates a wrapper function that conditionally executes and prints the result of the decorated function.
    The wrapper only executes the original function when exactly one argument is provided.
    The result of the function call is then printed to stdout.
    Args:
        func: The function to be decorated

    Returns:
        A wrapper function that takes any number of arguments and conditionally executes func
    """
    def wrapper(*args):
        if len(args) == 1:
            print(func(*args))

    return wrapper