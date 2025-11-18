from task_3 import progress


def sum_progress(a1, r, n: int) -> int:
    """
    function, counting sum of first n numbers of progression
    :param a1: first num of progression
    :param r: progress diff
    :param n: index of last number in sum
    :return: progression_sum
    """
    match n:
        case 1:
            return a1

    return progress(a1, r, n) + sum_progress(a1, r, n - 1)


