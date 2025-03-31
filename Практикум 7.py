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



