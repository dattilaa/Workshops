def combin(n, k: int) -> int:
    """
    function, counting number of combinations
    of k elements from n
    :param n: elements available
    :param k: number of elements if one combination
    :return: number of combinations
    """
    match k:
        case 0:
            return 1

    if k > n or k < 0:
        return 0

    return combin(n - 1, k - 1) + combin(n - 1, k)


