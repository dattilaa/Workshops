import itertools


def subsets_list(s: set) -> list[set]:
    """
    Returns list of all users set's subsets
    :param s: users set
    :return: subsets list
    """
    s_list = list(s)
    subsets = []

    for r in range(len(s) + 1):
        subsets.extend(itertools.combinations(s_list, r))

    return [set(subset) for subset in subsets]


def main() -> None:
    user_set = set(map(int, input().split()))
    print(subsets_list(user_set))


if __name__ == '__main__':
    main()