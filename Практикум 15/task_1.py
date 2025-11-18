def pownum(a, n: int) -> int:
    """
    function, raising a number to a power of another num
    :param a: base number
    :param n: degree
    :return: answer
    """
    match n:
        case 1:
            return a
    return a * pownum(a, n - 1)

print(pownum(2, 5))