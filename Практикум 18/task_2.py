def multiples(a, b, c, d: int) -> int:
    """
    Calculates the sum of numbers in a range that are multiples of two given divisors.
    The function considers all integers from a to b (inclusive) and sums those
    that are divisible by both c and d.

    Args:
        a: The starting integer of the range (inclusive)
        b: The ending integer of the range (inclusive)
        c: The first divisor
        d: The second divisor

    Returns:
        The sum of all numbers in the range [a, b] that are divisible by both c and d
    """
    numbers = [num for num in range(a, b + 1)]
    multiple_nums = list(filter(lambda x: not x % c and not x % d, numbers))

    return sum(multiple_nums)


def main() -> None:
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(multiples(a, b, c, d))


if __name__ == '__main__':
    main()
