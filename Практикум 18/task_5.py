import functools as f
import math as m

def main() -> None:
    a, b = map(int, input().split())
    c = int(input())

    square_nums = [num for num in range(a, b + 1)
                   if int(m.sqrt(num) ** 2) == num]
    certain_nums = [num for num in square_nums if not num % c]

    print(f.reduce(lambda x, y: x * y, certain_nums))


if __name__ == '__main__':
    main()


