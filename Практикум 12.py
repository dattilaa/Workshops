# Task 1
line = input()
counter = 0
max_count = 0

for i in line:
    if i == ' ':
        counter += 1
    else:
        if counter > max_count:
            max_count, counter = counter, 0

print(max_count)
print('---------------------------')

# Task 2
line = input()
counter = 0
max_count = 0

for i in range(1, len(line)):
    if line[i] == line[i-1]:
        counter += 1
    else:
        if counter > max_count:
            max_count, counter = counter, 0

print(max_count)
print('---------------------------')

# Task 3
line = input()
letters = set()

for i in line:
    letters.add(i)

print(len(letters))
print('---------------------------')

# Task 4
text = input()
for i in text:
    if text.count(i) == 3:
        print(i)
        break
print('---------------------------')

# Task 5
text1, text2, text3 = input().split()
letters, unique_letters = set(), set()
words = [text1, text2, text3]

for i in range(len(words)):
    word = words[i]
    words.pop(i)
    for j in words:
        for k in j:
            letters.add(k)
    print(letters)
    for l in word:
        if l not in letters:
            unique_letters.add(l)
    words.insert(i, word)
    letters.clear()

print(unique_letters)
print('---------------------------')

# Task 6
text = input()
for i in range(len(text) - 1, 0, -1):
    if i == len(text) - 1:
        print(text[i].upper(), end='')
    else:
        print(text[i], end='')
print(text[0].lower())
print('---------------------------')

# Task 7
text = input()
min_len = float('+inf')
ru_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = [chr(i) for i in range(97, 123)]
for i in ru_l:
    alphabet.append(i)

if text[-1] in alphabet:
    text += ' '

for i in text.lower():
    if i not in alphabet:
        ind = text.find(i)
        word = text[:ind]
        text = text[ind + 1:]
        if len(word) < min_len:
            min_len = len(word)

print(min_len)
print('---------------------------')

# Task 8
text = input()
ru_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = [chr(i) for i in range(97, 123)]
lens = []
words = {}
for i in ru_l:
    alphabet.append(i)

if text[-1] in alphabet:
    text += ' '

for i in text.lower():
    if i not in alphabet:
        ind = text.find(i)
        word = text[:ind]
        lens.append(len(word))
        words[len(word)] = word
        text = text[ind + 1:]

lens.sort(reverse=True)

for j in lens:
    print(words.get(j), end=' ')
print('---------------------------')

# Task 9
text = input()
min_len = float('+inf')
ru_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = [chr(i) for i in range(97, 123)]
words = []
for i in ru_l:
    alphabet.append(i)

if text[-1] in alphabet:
    text += ' '

for i in text.lower():
    if i not in alphabet:
        ind = text.find(i)
        word = text[:ind]
        if word not in words:
            words.append(word)
        else:
            print(word)
            break
print('---------------------------')

# Task 10
text = input()
min_len = float('+inf')
ru_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = [chr(i) for i in range(97, 123)]
words = []
for i in ru_l:
    alphabet.append(i)

if text[-1] in alphabet:
    text += ' '

for i in text.lower():
    if i not in alphabet:
        ind = text.find(i)
        word = text[:ind]
        if word not in words:
            words.append(word)
        text = text[ind + 1:]

for k in words[1:]:
    flag = True
    for m in k:
        if k.count(m) > 1:
            flag = False
    if not flag:
        words.remove(k)

print(words[1:])
print('---------------------------')

# Task 11
turn = 1
city = input()
while city.lower() != 'не знаю':
    turn += 1
    prev_city, city = city, input()
    if prev_city[-1] in ['ь', 'ы']:
        if prev_city[-2] != city[0].lower():
            break
    else:
        if prev_city[-1] != city[0].lower():
            break

if city.lower() == 'не знаю':
    turn -= 1
if turn % 2:
    print('Победил Петя')
else:
    print('Победил Вася')
print('---------------------------')

# Task 12
import keyword as kw

alphabet = [chr(i) for i in range(97, 123)]
nums = [str(i) for i in range(10)]
print(nums)
symbols = alphabet + nums
symbols.append('_')
name = input()

if not kw.iskeyword(name) and name[0] not in nums:
    print(name[0])
    flag = True
    for i in name[1:]:
        if i not in symbols:
            flag = False
            print('Не может быть именем')
            break
    if flag:
        print('Может быть именем')
else:
    print('Не может быть именем')
print('---------------------------')

# Task 13
def lucky(n):
    if len(n) % 2:
        return False
    s1, s2 = 0, 0
    for i in range(len(n)):
        if i < 3:
            s1 += int(n[i])
        else:
            s2 += int(n[i])
    return True if s1 == s2 else False

counter = 1
while not lucky(num := str(int(input()))):
    counter += 1

print(counter)
print('---------------------------')

# Task 14
def field_of_dreams():
    hint = input('Введите подсказку: ')
    word = input('Введите загаданное слово: ').lower()

    print('\n' * 25)

    letters = set()
    attempts = 10

    print(hint)

    while attempts > 0:
        display_word = ''
        for l in word:
            if l in letters or l == ' ':
                display_word += l
            else:
                display_word += '*'

        print(display_word)

        if display_word == word:
            print('Победа!')
            return


        action = input('Буква или слово (0 - буква, 1 - слово)? ')
        match action:
            case '0':
                letter = input('Введите букву: ').lower()

                if len(letter) != 1:
                    print('Введите одну букву!')
                    continue

                if letter in letters:
                    print('Эта буква уже была!')
                    continue

                letters.add(letter)

                if letter not in word:
                    attempts -= 1
                    print(f'Такой буквы нет! Осталось попыток: {attempts}')

            case '1':
                guess = input("Введите слово: ").lower()

                if guess == word:
                    print("Победа!")
                    return
                else:
                    attempts -= 1
                    print(f'Неверно! Осталось попыток: {attempts}')
            case _:
                print('Неверный выбор! Выберите 0 или 1.')

    print('Проигрыш!')
    print(f'Загаданное слово было: {word}')

field_of_dreams()
print('---------------------------')

# Task 15
def cows_and_bulls():
    while True:
        num = input('Введите число: ')

        if len(num) != 4 or not num.isdigit():
            print('Число должно быть четырехзначным')
            continue
        elif len(set(num)) != 4:
            print('Цифры не должны повторяться')
            continue
        break

    print('\n' * 25)

    attempts = 10
    for i in range(attempts):
        while True:
            n = input('Введите четырехзначное число с неповторяющимися цифрами: ')

            if len(n) != 4 or not n.isdigit():
                print('Число должно быть четырехзначным')
                continue
            elif len(set(n)) != 4:
                print('Цифры не должны повторяться')
                continue
            break

        cows, bulls = 0, 0
        for j in range(4):
            if n[j] == num[j]:
                bulls += 1
            elif n[j] in num:
                cows += 1

        print(f'Быков: {bulls} Коров: {cows}')

        if bulls == 4:
            print('Победа')
            return

    print('Проигрыш!')

cows_and_bulls()
print('---------------------------')

# Task 16
def check_chars(text):
    chars = []
    for s in text:
        if s == '(':
            chars.append(s)
        elif s == ')':
            if not chars:
                return False
            chars.pop()

    return not len(chars)

print(check_chars(input()))
print('---------------------------')

# Task 17-20...































