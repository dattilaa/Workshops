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
            if l in letters:
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
