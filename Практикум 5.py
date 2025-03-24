# Task 1
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print(366)
elif year % 400 == 0:
    print(366)
else:
    print(365)
print('---------------------------')

# Task 2
import turtle as trt
xc = int(input('xc = '))
yc = int(input('yc = '))
r = int(input('r = '))
x = int(input('x = '))
y = int(input('y = '))

trt.penup()
trt.setpos(xc, yc)
trt.right(90)
trt.forward(r)
trt.left(90)
trt.pendown()
trt.circle(r)
trt.penup()
trt.home()

trt.setpos(x, y)
trt.dot(10, 'red')

if (xc - x) ** 2 + (yc - y) ** 2 > r ** 2:
    trt.write('Точка вне окружности')
else:
    trt.write('Точка внутри окружности')
print('---------------------------')

# Task 3
n = int(input())
num = n
m = 0
while n:
    m *= 10
    m += n % 10
    n //= 10
if num == m:
    print('настоящее')
else:
    print('кривое')
print('---------------------------')

# Task 4
n = int(input())
m = n % 10
if m == 1 and n != 11:
    print(f'{n} попугай')
elif m > 1 and m < 5 and (n < 11 or n > 20):
    print(f'{n} попугая')
else:
    print(f'{n} попугаев')
print('---------------------------')

# Task 5
weight_lb = int(input('Введите вес в фунтах: '))
height_inch = int(input('Введите рост в дюймах: '))
w_kg = weight_lb / 2.20462
h_m = height_inch * 0.0254
BMI = round(w_kg / (h_m ** 2), 2)
if BMI < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= BMI <= 18.49:
    print('Недостаточная масса тела')
elif 18.5 <= BMI <= 24.99:
    print('Норма')
elif 25 <= BMI <= 29.99:
    print('Избыточная масса тела')
elif 30 <= BMI < 35:
    print('Ожирение I степени')
elif 35 <= BMI < 40:
    print('Ожирение II степени')
else:
    print('Ожирение III степени')
print('---------------------------')

# Task 6
counter = 0
n1, n2, n3 = map(int, input().split())
if n1 == n2 and n1 == n3:
    counter += 3
elif n1 == n2 or n1 == n3 or n2 == n3:
    counter += 2
else:
    counter += 1
print(counter)
print('---------------------------')

# Task 7
n, k, m = map(int, input().split())
counter = 0
if m < k:
    m += n
for i in range(k + 1, m):
    counter += 1
print(counter)
print('---------------------------')

# Task 8
k = int(input())
g = k // 29 // 17
s = k // 29 % 17
if g == 0:
    print(f'{s} сиклей')
    print(f'{k % 29 % 17} кнатов')
if s == 0:
    print(f'{g} галлеонов')
    print(f'{k % 29 % 17} кнатов')
if k % 29 % 17 == 0:
    print(f'{g} галлеонов')
    print(f'{s} сиклей')
print('---------------------------')

# Task 9
h1, h2, h3 = map(int, input().split())
max_h = max(h1, h2, h3)
min_h = min(h1, h2, h3)
mid_h = h1 + h2 + h3 - max_h - min_h
print(max_h, mid_h, min_h)
print('---------------------------')

# Task 10
pin = int(input())
if pin // 1000 > 9:
    print('ERROR')
else:
    n1 = pin // 1000
    n2 = pin // 100 % 10
    n3 = pin // 10 % 10
    n4 = pin % 10
    if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
          print('ERROR')
    else:
        if 1900 <= pin <= 2050:
            print('ERROR')
        else:
            print('OK')
print('---------------------------')



