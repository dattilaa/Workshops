def is_plural(nums: list, n: int) -> bool:
    """
    Checking if n enters nums list more than one time
    :param nums: numbers sequence
    :param n: users number
    :return: True, False
    """
    unique, duplicates = set(), set()
    for num in nums:
        if num in unique:
            duplicates.add(num)
        else:
            unique.add(num)

    return n in duplicates

def main() -> None:
    numbers = list(map(int, input().split()))
    n = int(input())
    print(is_plural(numbers, n))


if __name__ == '__main__':
    main()


