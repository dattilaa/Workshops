# Task 1
print('Hello, python!')
print('---------------------------')

# Task 2
print('Привет,Python!')
print('Hello,Python!')
print('Bonjour,Python!')
print('Hej,Python!')
print('Hola,Python!')
print('---------------------------')

# Task 3
print('Привет', 'Python!', sep = ' ')
print('---------------------------')

# Task 4
print('(\___/)', '(=\'.\'=)', '(")_(")', sep = '\n')
print('---------------------------')

# Task 5
print('Привет,Python!', 'Hello,Python!', 'Bonjour,Python!', 'Hej,Python!', 'Hola,Python!', sep = '\n')
print('---------------------------')

# Task 6
name = input('Как вас зовут? ')
print('Здравствуйте,', name)
print('---------------------------')

# Task 7
name = input('Как вас зовут?' )
print('Здравствуйте,', name)
hobby = input('Что вам нравится? ')
print('Отлично!', hobby, '- хорошее увлечение.')
print('---------------------------')

# Task 8
login = input('Login: ')
password = input('Password: ')
newpass = input('New password: ')
print('User', login, 'has changed the password to', newpass)
print('---------------------------')

# Task 9
song1 = input('Введите плей-лист папы:\n')
song2 = input()
song3 = input()
song4 = input()
song5 = input()
print('Плейлист мамы:', song5, song4, song3, song2, song1, sep = '\n')
print('---------------------------')

# Task 10
flight_n = int(input('Номер рейса: '))
name_ru = input('Название авиакомпании (на русском языке): ')
name_eng = input('Название авиакомпании (на английском языке): ')
dest_ru = input('Город прилета (на русском языке): ')
dest_eng = input('Город прилета (на английском языке): ')
print('Заканчивается посадка на рейс', flight_n, name_ru, 'до города', dest_ru)
print('This is the final call for', name_eng, 'flight', flight_n, 'to', dest_eng)
print('---------------------------')

# Task 11
name = input('Как вас зовут? ')
print('Привет, ', name, '!', sep = '')
print('---------------------------')

# Task 12
total_cost = int(input('Введите общую стоимость часов: '))
price_ag = 48
quantity_ag = 96
quantity_au = quantity_ag/16
rev_au = total_cost - price_ag*quantity_ag
print('Стоимость золотых часов:', rev_au/quantity_au)
print('---------------------------')

# Task 13
import math as m
signal_radius = int(input('Введите радиус дальности приема: '))
dead_radius = int(input('Введите радиус мертвой зоны: '))
print('Площадь покрываемой территории:', abs(m.pi*signal_radius**2 - m.pi*dead_radius**2))
print('---------------------------')

# Task 14
# Simplified algorithm: 4 is substracted from each number
your_number = int(input('Введите число: '))
print('Полученный результат:', ((your_number + 2)*3 - 6)/3 - 4)
print('Площадь покрываемой территории:', abs(m.pi*signal_radius**2 - m.pi*dead_radius**2))
print('---------------------------')

# Task 15
length_cm = float(input('Введите расстояние в сантиметрах: '))
print('Ваше расстояние в дюймах: ', length_cm/2.54)
print('Ваше расстояние в футах: ', length_cm/30.48)
print('Ваше расстояние в ярдах: ', length_cm/91.44)
print('Ваше расстояние в милях: ', length_cm/160934.4)


