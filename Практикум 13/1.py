import re

def count_chars(text):
    vowels_count = 0
    consonants_count = 0
    vowels = ['а', 'о', 'у', 'ы', 'э'
              'я', 'ё', 'ю', 'и', 'е']
    re_text = re.sub(r'[^а-яА-Я]','', text)
    for i in re_text.lower():
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

    print(f'Кол-во гласных: {vowels_count}')
    print(f'Кол-во согласных: {consonants_count}')


user_text = input()
count_chars(user_text)
