# Task 1
total_cost = int(input('Введите общую стоимость часов: '))
price_ag = 48
quantity_ag = 96
quantity_au = quantity_ag/16
rev_au = total_cost - price_ag*quantity_ag
print('Стоимость золотых часов:', int(rev_au/quantity_au))
print('---------------------------')

# Task 2
name_pt1, name_pt2 = input('Введите название страны: ').split()
print(name_pt1, name_pt2, sep = '\n')
print('---------------------------')

# Task 3
s, r = map(int, input().split())
print(s+r)
print('---------------------------')

# Task 4
print(2+7**4, 'людей и животных направляются в Сент-Айвс.')
print('---------------------------')

# Task 5
q_predict = float(input('Введите плановый объем продаж: '))
print('Ожидаемая прибыль:', round(q_predict*0.19, 2))
print('---------------------------')

# Task 6
weight_lb = int(input('Введите вес в фунтах: '))
height_inch = int(input('Введите рост в дюймах: '))
w_kg = weight_lb/2.20462
h_m = height_inch*0.0254
print('Ваш ИМТ:', round(w_kg/(h_m**2), 2))
print('---------------------------')

# Task 7
v_litres = 100000*1/1000
print(f'Объем осадков: {v_litres} литров.')
print('---------------------------')

# Task 8
N, M = map(int, input().split())
print(M//(N+1), 'конфет достанется каждому.')
print('---------------------------')

# Task 9
N = int(input('Количество добытых быков: '))
K = int(input('Количество семей: '))
print(f'{N%K}. Столько быков будет отпущено.')
print('---------------------------')

# Task 10
import math as m
dist_m = int(input('Расстояние в метрах, которое прошла Фейт: '))
print(f'{m.floor(dist_m/1609.34)}. Столько полных миль прошла Фейт.')