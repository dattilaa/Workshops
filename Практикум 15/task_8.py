def fib(k: int) -> int:
    """
    function, counting kth term of fib sequence
    :param k: desirable fib nums index
    :return: kth term
    """
    if k < 3:
        return 1

    return fib(k - 2) + fib(k - 1)


