def count(a, b: int) -> int:
    """
    function, returning amount of biggest squares
    we can cut from axb rectangle
    :param a: width
    :param b: height
    :return: squares_num
    """
    if a == b:
        return 1

    if a < b:
        a, b = b, a

    squares_num = a // b
    if not a % b:
        return squares_num

    return squares_num + count(b, a % b)



