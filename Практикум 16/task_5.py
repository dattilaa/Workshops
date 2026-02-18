def sieve_of_eratosthenes(n: int) -> list:
    """
    Shows all prime numbers less than special number
    :param n: users number
    :return: primes_list
    """
    nums = set(i for i in range(2, n + 1))
    for num in sorted(nums):
        aliquots = set(aliquot for aliquot in range(num ** 2, n + 1) if not aliquot % num)
        nums -= aliquots

    return sorted(list(nums))


def main() -> None:
    print(sieve_of_eratosthenes(int(input())))


if __name__ == '__main__':
    main()




