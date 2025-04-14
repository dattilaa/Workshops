# Task 1
n, d, r = map(int, input().split())
l = 0
for i in range(n):
    l += r * 2 + (-1) ** i * d * 2
print(l)
print('---------------------------')

# Task 2
while (n := int(input())) <= 2:
    continue
while n >= 2:
    print(f'{n ** 0.5:.3f}')
    n **= 0.5
print('---------------------------')

# Task 3
n = int(input())
quantity = []
for i in range(1, n + 1):
    if not (n % i) and i > 1:
        quantity.append(n // i)
quantity.sort()
print(n // quantity[-1])
print('---------------------------')

# Task 4
counter = 0
v = 0
while (n := int(input())) != 0:
    v = n + 3
    if v % 9 == 0:
        counter += 1
print(counter)
print('---------------------------')

# Task 5
list_1, list_2 = [], []
flag = True
for i in range(100000, 1000000):
    for j in range(1, 4):
        if str(i)[j - 1] == str(i)[-j]:
            list_1.append(i)

for k in list_1:
    for l in range(1, 3):
        if str(k - 1)[l] == str(k - 1)[-l - 1]:
            list_2.append(k - 1)

for n in list_2:
    for m in range(1, 4):
        if str(n - 1)[m] == str(n - 1)[-m]:
            flag = False
    if not flag:
        print(n)
print('---------------------------')

# Task 6
for i in range(10, 100):
    if i ** 2 % 100 == i:
        print(f'{i:>3}\n*{i}\n___\n{i ** 2}')
        break
print('---------------------------')

# Task 7
flag = True
for i in range(10000, 100000):
    m = str(i // 10000)
    o = str(i // 1000 % 10)
    n = str(i // 100 % 10)
    e = str(i // 10 % 10)
    for j in range(0, 10):
        for k in range(0, 10):
            send = int(str(j) + e + n + str(k))
            more = int(m + o + str(j) + e)
            money = int(m + o + n + e + str(j))
            if send + more == money:
                print(f'{send:>5}\n+{more}\n_____\n{money}')
                flag = False
        if not flag:
            break
print('---------------------------')

# Task 8
import math as mt
x = int(input())
counter = 0
adds = [i for i in range(1, mt.ceil(x ** 0.5))]
for j in adds:
    for k in adds:
        if j ** 2 + k ** 2 == x:
            counter += 0.5
print(f'{counter:.0f}')
print('---------------------------')

# Task 9
n = int(input())
counter_1, counter_2 = 0, 0
for i in range(n + 1):
    counter_1 += i
    for j in range(n + 1):
        counter_2 += j
print((counter_1 + counter_2) // 2)
print('---------------------------')

# Task 10
def count_staircases(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for m in range(N + 1):
        dp[0][m] = 1
    for k in range(1, N + 1):
        for m in range(1, N + 1):
            if m > k:
                dp[k][m] = dp[k][k]
            else:
                dp[k][m] = dp[k][m - 1] + dp[k - m][m - 1]
    return dp[N][N] - 1


N = int(input())
if N > 100:
    print('Ошибка')
else:
    print(f"Количество возможных лесенок: {count_staircases(N)}")







