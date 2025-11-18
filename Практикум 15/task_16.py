def digits(n: int) -> str:
    """
    function, returning converted all converted digits
    :param n: desirable number system
    :return: digits
    """
    nums = [str(i) for i in range(10)] + [chr(j) for j in range(ord('A'), ord('A') + n - 10)]
    return ''.join(nums)


def check_n(n: int) -> bool:
    """
    function, checking if n  is relevant
    :param n: desirable
    :return: True, False
    """
    if 2 <= n <= 16:
        return True
    return False


def ten_to_n(x, n: int) -> str:
    """
    function, converting number from decimal to nth number system
    :param x: users number
    :param n: desirable number system
    :return: nth_number
    """
    if x < n:
        return digits(n)[x]

    return ten_to_n(x // n, n) + digits(n)[x % n]





