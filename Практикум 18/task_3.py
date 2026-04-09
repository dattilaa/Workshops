def main() -> None:
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    nums = [num for num in range(a, b + 1)]
    certain_nums = list(map(lambda x: 1 if x % c and x % 10 == d else 0, nums))
    print(sum(certain_nums))




if __name__ == '__main__':
    main()
