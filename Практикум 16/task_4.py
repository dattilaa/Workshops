def is_in_intersection(n: int, set_1: set, set_2: set) -> bool:
    """
    Shows if number lays in intersection of two sets
    :param n: users number
    :param set_1: first set
    :param set_2: second set
    :return: True, False
    """
    return n in set_1 & set_2


def main() -> None:
    set_1 = set(map(int, input().split()))
    set_2 = set(map(int, input().split()))
    n = int(input())

    print(is_in_intersection(n, set_1, set_2))


if __name__ == '__main__':
    main()

