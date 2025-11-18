def progress(a1, r, n: int) -> int:
    """
    function, counting nth number of progression
    :param a1: first number of progression
    :param r: progress diff
    :param n: index of term user wants
    :return: a_n
    """
    match n:
        case 1:
            return a1

    return r + progress(a1, r, n - 1)


