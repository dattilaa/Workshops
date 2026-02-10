import itertools


def k_len_subsets(s: set, k: int) -> list[set]:
    """
    Returns all subsets of base set with length k
    :param s: users set
    :param k: length of subset
    :return: subsets list
    """
    s_list = list(s)
    subsets = list(itertools.combinations(s_list, k))

    return [set(subset) for subset in subsets]


def main() -> None:
    user_set = set(map(int, input().split()))
    while (k := int(input())) > len(user_set):
        continue

    print(k_len_subsets(user_set, k))


if __name__ == '__main__':
    main()