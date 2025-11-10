def dividers(n: int) -> list:
    """
    function, returning all nums dividers
    :param n: number
    :return: dividers
    """
    divs = set()
    divs.add(1)
    divs.add(n)

    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            divs.add(i)
            divs.add(n // i)

    return sorted(list(divs))


print(dividers(int(input())))