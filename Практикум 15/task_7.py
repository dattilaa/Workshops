def nod(a, b: int) -> int:
    """
    function, counting gcd of two users numbers
    :param a: first user number
    :param b: second user number
    :return: gcd
    """
    if a < b:
        a, b = b, a
    if not a % b:
        return b

    return nod(b, a % b)


print(nod(100, 75))