def numbers(x: int):
    """
    function, printing user nums digits in reversed order
    :param x: users num
    :return: None
    """
    print(x % 10)
    if x > 9:
        numbers(x // 10)


numbers(1234)
