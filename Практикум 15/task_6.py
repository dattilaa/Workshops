def isdegree5(n: int) -> bool:
    """
    function, showing if number is power of five
    :param n: user number
    :return: True, False
    """
    match n:
        case 5:
            return True
    return isdegree5(n // 5) if not n % 5 else False


def degree5(n) -> int:
    """
    function, counting 'five' power of number
    :param n: user number
    :return: degree
    """
    if isdegree5(n):
        match n:
            case 5:
                return 1
        return 1 + degree5(n // 5)

    return -1


print(degree5(125))