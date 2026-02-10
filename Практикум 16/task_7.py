import itertools


def main() -> None:
    users_set = set(map(int, input().split()))
    print(list(itertools.permutations(users_set)))


if __name__ == '__main__':
    main()