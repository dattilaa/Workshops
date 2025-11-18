def count(n: int) -> int:
    """
    function, returning amount of digits in number
    :param n: users number
    :return: counter
    """
    match n:
        case 1:
            return 1

    return 1 + count(n // 10)

