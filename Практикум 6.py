# Task 1
import math as mt
a, b = map(int, input().split('x'))
if (a / 2) ** 2 + (b / 2) ** 2 <= 6.5 ** 2:
    print('Да')
else:
    print('Нет')
print('---------------------------')

# Task 2
a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))

if ((a <= c and b <= d) or (a <= d and b <= c) or
    (a <= c and b <= e) or (a <= e and b <= c) or
    (a <= d and b <= e) or (a <= e and b <= d)):
    print('да')
else:
    print('нет')
print('---------------------------')

# Task 3
n, m = map(int, input().split('x'))
k = int(input())
counter = 0
print('---------------------------')

if k < m * n:
    for line in range(1, n):
        if (line * m) >= k and ((n - line) * m) >= (n * m - k):
            counter += 1
    for column in range(1, m):
        if (column * n) >= k and ((m - column) * n) >= (n * m - k):
            counter += 1
else:
    print('Некорректный ввод')

if counter > 0:
    print('Успешно')
else:
    print('Неосуществимо')
print('---------------------------')

#4
cell = input('Введите клетку: ')
l = cell[:1]
n = int(cell[1:])
if l == 'a' or l == 'c' or l == 'e' or l == 'g':
    if n == 1 or n == 3 or n == 5 or n == 7:
        print('Чёрный')
    else:
        print('Белый')
elif l == 'b' or l == 'd' or l == 'f' or l == 'h':
    if n == 1 or n == 3 or n == 5 or n == 7:
        print('Белый')
    else:
        print('Чёрный')
print('---------------------------')

#5
letters = ['a','b','c','d','e','f','g','h']
inf = input('Введите ход: ')
start, end = inf.split('-')
for i in range(8):
    if start[0] == letters[i]:
        if letters[i - 1] == end[0] or letters[i+1] == end[0]:
            if (int(start[1]) + 2 == int(end[1]) or
                    int(start[1]) - 2 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')
        elif letters[i - 2] == end[0] or letters[i + 2] == end[0]:
            if (int(start[1]) + 1 == int(end[1]) or
                    int(start[1]) - 1 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')
print('---------------------------')

#6
n, k, m = map(int, input().split())
answ = (n // k) * 2 * m
print(answ)
print('---------------------------')

#7
k = int(input('Введите количество: '))
counter = 0
for i in range(k):
    if k % 5 == 0 and k > 4:
        c+=1
    else:
        k -= 7
for j in range(k):
    if k % 7 == 0 and k > 6:
        counter += 1
    else:
        k -= 5
if counter > 0:
    print('да')
else:
    print('нет')
print('---------------------------')

#8
position = int(input('Введите порядковый номер цифры: '))
current_position = 1
if position == current_position:
    print(0)
current_position += 1
for number in range(1, 201):
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if current_position == position:
            print(digit)
        current_position += 1
print('---------------------------')

#9
xc1 = float(input('Xc 1: '))
yc1 = float(input('Yc 1: '))
r1 = float(input('R1: '))
xc2 = float(input('Xc 2: '))
yc2 = float(input('Yc 2: '))
r2 = float(input('R2: '))
print('---------------------------')

distance = ((xc2 - xc1) ** 2 + (yc2 - yc1) ** 2)**0.5
if distance > r1 + r2:
    print('Окружности лежат одна вне другой, не касаясь')
elif distance < abs(r1 - r2):
    print('Одна окружность лежит внутри другой, не касаясь')
elif distance == r1 + r2:
    print('Окружности имеют внешнее касание')
elif distance == abs(r1 - r2):
    print('Окружности имеют внутреннее касание')
else:
    print('Окружности пересекаются')
print('---------------------------')

#10
coord_U_L_1 = input()
coord_D_R_1 = input()
coord_U_L_2 = input()
coord_D_R_2 = input()
x1_l, y1_u = map(float, coord_U_L_1.split(';'))
x1_r, y1_d = map(float, coord_D_R_1.split(';'))
x2_l, y2_u = map(float, coord_U_L_2.split(';'))
x2_r, y2_d = map(float, coord_D_R_2.split(';'))
if x1_r < x2_l or x2_r < x1_l or y2_u < y1_d or y1_u < y2_d:
    print('Прямоугольники лежат вне друг-друга, не касаясь')
elif (x1_r == x2_l or x1_l == x2_r) and (y1_d < y2_u and y1_u > y2_d):
    print('Прямоугольники имеют касание')
elif (y1_u == y2_d or y1_d == y2_u) and (x1_l < x2_r and x1_r > x2_l):
    print("Прямоугольники имеют касание")
elif (x1_l > x2_l and x1_r < x2_r and y1_d > y2_d and y1_u < y2_u):
    print("Первый прямоугольник полностью внутри второго, не касаясь")
elif (x2_l > x1_l and x2_r < x1_r and y2_d > y1_d and y2_u < y1_u):
    print("Второй прямоугольник полностью внутри первого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")