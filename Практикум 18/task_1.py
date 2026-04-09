def count_upper(user_str: str, i, j: int) -> int:
    """
    Counts the number of uppercase letters in a substring.

    The substring is extracted from index i-1 to j-1 (1-based indexing).

    Args:
        user_str: The input string to search within
        i: The starting position of the substring (1-based indexing)
        j: The ending position of the substring (1-based indexing)

    Returns:
        The number of uppercase characters in the specified substring
    """
    upper_chars = list(filter(lambda x: x == x.upper(), user_str[i - 1:j - 1]))
    return len(upper_chars)


def main() -> None:
    user_str = input()
    i, j = map(int, input().split())
    print(count_upper(user_str, i, j))


if __name__ == '__main__':
    main()
