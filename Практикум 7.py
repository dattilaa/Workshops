# Task 1
counter = 0
for i in range(100, 1000):
    if i % 17 == 0:
        print(i, end=' ')
        counter += 1
print(f'\n{counter}')
print('---------------------------')

# Task 2
counter = 0
for i in input():
    counter += 1
    if counter % 3 == 0:
        print(i, end='')
print('---------------------------')

# Task 3
while (n := int(input())) ** 0.5 * 10 % 10 != 0:
    print('Введите другое число:')
print('Это число является полным квадратом')
print('---------------------------')

# Task 4
n = int(input())
counter = 0
for i in range(1, n + 1):
        counter += i
        if i == n:
            print(f'{i} = {counter}')
        else:
            print(f'{i} + ', end='')
print('---------------------------')

# Task 5
n = int(input())
for i in range(1, n):
    if i ** 3 >= n:
        break
    print(i ** 3, end=' ')
print('---------------------------')

# Task 6
n = int(input())
sub = 1
while sub <= n:
    print(sub)
    sub *= 2
print('---------------------------')

# Task 7
answer = int(input())
flag = True
while answer != 2:
    answer /= 2
    if int(answer) % 2 != 0:
        flag = False
        break
if not flag:
    print('Неверно')
else:
    print('Верно')
print('---------------------------')

# Task 8
n = int(input())
counter = 0
while n >= 1:
    counter += 1
    n //= 2
print(counter)
print('---------------------------')

# Task 9
n, k, r = map(int, input().split())
counter = 1
per = k / 100
while n < r:
    counter += 1
    n *= (1 + per)
print(counter)
print('---------------------------')

# Task 10
counter = 0
prev_temp = 0
while (temp := float(input())) != 0:
    if 37.4 <= temp <= 37.8:
        if temp < prev_temp:
            counter += 1
        prev_temp = temp
    else:
        continue
print(counter)

