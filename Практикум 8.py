# Task 1
results = []
while (result := int(input())) != -1:
    results.append(result)
results.sort()
print(results[-1])
print('---------------------------')

# Task 2
friends = 0
while (result := int(input())) != -1:
    friends += 1
print(friends)
print('---------------------------')

# Task 3
counter = 0
salary_sum = 0
while (salary := int(input())) != 0:
    counter += 1
    salary_sum += salary
print(salary_sum / counter)
print('---------------------------')

# Task 4
sum = 0
for i in range(1, n := int(input()) + 1):
    sum += i
    print(sum)
print('---------------------------')

# Task 5
sum = 0
counter = 0
for i in range(2, n := int(input())):
    for j in range(1, n):
        if not (i % j) and j != i:
            sum += j
    if sum == i:
        counter += 1
    sum = 0
print(counter)
print('---------------------------')

# Task 6
for i in range (1, n := int(input()) + 1):
    print(f'{'*' * i:>{n}}')
print('---------------------------')

# Task 7
num = input('Введите целое число: ')
while not num.isdigit():
    num = input('Ошибка. Попробуйте еще раз. Введите число: ')
print(f'Введено целое число: {num}')
print('---------------------------')

# Task 8
n1, n2, n3 = '', '', ''

#1
for i in range(1, 10):
    n1 += str(i)
    print(f'{n1} * 8 + {i} = {int(n1) * 8 + i}')
    print('\n')

#2
for j in range(1, 10):
    n2 += str(j)
    print(f'{n2} * 9 + {j + 1} = {int(n2) * 9 + (j + 1)}')
    print('\n')

#3
for n in range(1, 10):
    n3 += '1'
    print(f'{n3} * {n3} = {int(n3) ** 2}')
print('---------------------------')

# Task 9
counter = 0
n = int(input())
for i in range(2, n + 1):
    for j in range(2, i // 2 + 1):
        if not (i % j):
            counter += 1
    if counter == 0:
        print(i)
    counter = 0
print('---------------------------')

# Task 10
sum = 0
counter = 0
for i in range(2, n := int(input())):
    for j in range(1, n):
        if not (i % j) and j != i:
            sum += j
    if sum == i:
        counter += 1
        print(i)
    sum = 0








