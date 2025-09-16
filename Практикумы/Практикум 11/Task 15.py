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
