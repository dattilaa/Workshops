def function1(x: int, d=2) -> int:
    """
    function, checking if users number is prime
    :param x: users number
    :param d: base divider
    :return: 1, 0
    """
    if x <= 1:
        return 0

    if d ** 2 > x:
        return 1

    return function1(x, d + 1) if x % d else 0


