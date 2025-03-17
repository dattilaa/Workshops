# Task 1
if (input()) ==  'пароль':
    print('Проходи!')
else:
    print('Доступ запрещен!')
print('---------------------------')

# Task 2
print('Какие два слова передал первой радиограммой Александр Попов?')
w1 = input('Первое слово: ')
w2 = input('Второе слово: ')
if w1 == 'Я' and w2 == 'устал':
    print('Верно')
else:
    print('Неверно')
print('---------------------------')

# Task 3
print('Как зовут главного персонажа романов')
print('романов Яна Флеминга о вымышленном шпионе секретной')
name = input('разведывательной службе Великобритании? ')
match name:
    case 'Джеймс Бонд' | 'джеймс бонд':
        print('Верно')
    case _ :
        print('Неверно')
print('---------------------------')

# Task 4
print('Вы поедете на бал?')
answ = input('Ответ: ')
if answ != 'Да' and answ != 'да' and answ != 'Нет' and answ != 'нет':
    print('Верно')
else:
    print('Неверно')
print('---------------------------')

# Task 5
N, M = int(input()), int(input())
if N < M:
    print(N)
elif N > M:
    print(M)
else:
    print('Значения равны')
print('---------------------------')

# Task 6
score_1, score_2 = map(int, input().split(':'))
if score_1 > score_2:
    print(1)
elif score_1 < score_2:
    print(2)
else:
    print(0)
print('---------------------------')

# Task 7
k_score, a_score, s_score = map(int, input().split())
if k_score > a_score and k_score > s_score:
    print(k_score)
elif a_score > k_score and a_score > s_score:
    print(a_score)
else:
    print(s_score)
print('---------------------------')

# Task 8
name = input('Здравствуйте! Как вас зовут? ')
print(f'Очень приятно, {name}! Меня зовут Марк.')
age = int(input('Сколько вам лет? '))
mark_age = 2025 - 1944
if mark_age > age:
    print(f'Да, {name}, я старше вас на {mark_age - age}')
else:
    print(f'Да, {name}, я младше вас на {age - mark_age}')
enjoyment = input('Вам нравится программировать? ')
match enjoyment:
    case 'Да' | 'да':
        print('Превосходно! Уверен, у Вас получится написать')
        print('множество полезных и хороших программ.')
    case _ :
        print('Жаль. Я думал, что вы сможете написать')
        print('интересную программу для меня')
print('---------------------------')

# Task 9
ans_1 = input('Собака короткошерстной породы? ')
if ans_1 == 'Да' or ans_1 == 'да':
    ans_2 = input('Рост собаки меньше 50 см? ')
    if ans_2 == 'Да' or ans_2 == 'да':
        ans_3 = input('У собаки короткий хвост? ')
        if ans_3 == 'Да' or ans_3 == 'да':
            print('Английский бульдог')
        else:
            ans_4 = input('У собаки длинные уши? ')
            if ans_4 == 'Да' or ans_4 == 'да':
                print('Гончая')
            else:
                ans_5 = input('У собаки короткое тело? ')
                if ans_5 == 'Да' or ans_5 == 'да':
                    print('Мопс')
                else:
                    print('Чихуахуа')
    else:
        ans_3 = input('Собака весит более 50 кг? ')
        if ans_3 == 'Да':
            print('Датский дог')
        else:
            print('Фоксхаунд')
else:
    ans_2 = input('Рост собаки менее 50 см? ')
    if ans_2 == 'Да' or ans_2 == 'да':
        ans_3 = input('У собаки доброжелательный характер? ')
        if ans_3 == 'Да' or ans_3 == 'да':
            print('Кокер-спаниэль')
        else:
            print('Ирландский сеттер')
    else:
        ans_3 = input('Рост собаки менее 70 см? ')
        if ans_3 == 'Да' or ans_3 == 'да':
            ans_4 = input('У собаки длинные уши? ')
            if ans_4 == 'Да' or ans_4 == 'да':
                print('Большой вандейский грифон')
            else:
                print('Колли')
        else:
            ans_4 = input('Окрас рыжий с белыми отметинами? ')
            if ans_4 == 'Да' or ans_4 == 'да':
                print('Сенбернар')
            else:
                ans_5 = input('Белоснежный окрас? ')
                if ans_5 == 'Да' or ans_5 == 'да':
                    print('Ирландский волкодав')
                else:
                    print('Ньюфаундленд')
print('---------------------------')

# Task 10
num = int(input())
if num % 2 == 0:
    print('да')
else:
    print('нет')
print('---------------------------')


