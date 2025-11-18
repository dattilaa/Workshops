def simmetr(s: str, i, j: int) -> bool:
    """
    function, checking if 'i-j' slice is symmetrical
    :param s: users string
    :param i: start index
    :param j: end index
    :return: True, False
    """
    s.lower()
    if i >= j:
        return True
    if s[i] != s[j]:
        return False

    return simmetr(s, i + 1, j - 1)







