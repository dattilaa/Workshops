# Task 1
price = int(input('Введите стоимость биткоина: '))
print(str(price)[-3])
print('---------------------------')

# Task 2
time = int(input('Введите время в секундах: '))
print(f'{time // 3600} часов '
      f'{time // 60 % 60} минут '
      f'{time % 3600 % 60} секунд ')
print('---------------------------')

# Task 3
num = int(input('Введите число:\n'))
print(num%2)
print('---------------------------')

# Task 4
x, y, n = map(int, input().split())
print(f'Доход: {(x * 100 + y) * n // 100} руб. {(x * 100 + y) * n % 100} коп.')
print('---------------------------')

# Task 5
rep = int(input('Введите желаемое количество зайцев: '))
print('(\\___/) ' * rep)
print('(=\'.\'=) ' * rep)
print('(")_(") ' * rep)
print('---------------------------')

# Task 6
K = int(input())
N = int(input())
R = int(input())
print(int(str(K) * N) * R)
print('---------------------------')

# Task 7
# int was removed to make strings output being possible
raw = input('Enter number: ')
print(raw)
print('---------------------------')

# Task 8
import math
a = int(input())
b = int(input())
c = int(input())
cos_ang1 = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
cos_ang2 = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
ang_1 = math.degrees(math.acos(cos_ang1))
ang_2 = math.degrees(math.acos(cos_ang2))
ang_3 = 180 - ang_1 - ang_2
print(ang_1, ang_2, ang_3, sep='\n')
print('---------------------------')

# Task 9
ATT = int(input('Enter ATT value: '))
COMP = int(input('Enter COMP value: '))
YDS = int(input('Enter YARDS value: '))
TD = int(input('Enter ID value: '))
INT = int(input('Enter INT value: '))
a = (COMP / ATT - 0.3) * 5
b = (YDS / ATT - 3) * 0.25
c = TD / ATT * 20 + 2.375
d = INT / ATT * 25
Passer_rating = (a + b + c - d) / 6 * 100
print(f'Passer Rating: {Passer_rating}')
print('---------------------------')

# Task 10
x = int(input())
y = int(input())
print((x % y) * (y % x) + 1)
print('---------------------------')

# Task 11
deg = float(input())
seconds = 10800 / 90 * deg
print(f'{seconds // 3600:.0f} {seconds % 3600 // 60:.0f}')
print('---------------------------')

# Task 12
import datetime
print(datetime.datetime.now())
print('---------------------------')

# Task 13
import math as m
N = int(input('Введите количество строк: '))
C = int(input('Введите количество столбцов: '))
num = int(input('Введите порядковый номер: '))
page_num = 1 + num // (N * C + 1)
C_num = m.ceil((num % (N * C + 1) + page_num - 1) / N)
N_num = m.ceil(num % (N * C + 1) + page_num - 1 - N * (C_num - 1))
print(f'страница {page_num} столбец {C_num} строка {N_num}')


