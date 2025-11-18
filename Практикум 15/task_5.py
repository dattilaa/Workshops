def mod_number(a, b: int) -> int:
    """
    function, counting remainder of division
    :param a: dividend
    :param b: divider
    :return: remainder
    """
    if a < b:
        return a
    return mod_number(a - b, b)


print(mod_number(32, 5))