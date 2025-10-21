from math import gcd

def common_multiples(a, b, n):
    lcm = a * b / gcd(a, b)
    multiplier = 1
    while lcm * multiplier <= n:
        print(f'{lcm * multiplier:.0f}', end=' ')
        multiplier += 1


common_multiples(16, 24, 100)