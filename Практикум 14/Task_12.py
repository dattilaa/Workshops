import re


def count_letters_with_holes(text: str) -> int:
    """
    function, counting number of letters with holes in text
    :param text: user text
    :return: counter
    """
    hole_letters = {
        'english': ['A', 'B', 'D', 'O', 'P', 'Q', 'R',
                    'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'],
        'russian': ['А', 'Б', 'В', 'О', 'Р', 'Ф', 'Ю',
                    'а', 'б', 'в', 'е', 'о', 'р', 'ф', 'ю', 'э']
    }
    all_hole_letters = hole_letters['english'] + hole_letters['russian']
    counter = 0

    for char in text:
        if char in all_hole_letters:
            counter += 1

    return counter

user_text = input()
words = re.findall(r'\b\w+\b', user_text)
raw_text = ''.join(words)

hole_words = [word for word in words if count_letters_with_holes(word) >= 2]
holes_num = count_letters_with_holes(raw_text)

print(f'Количество букв с отверстиями: {holes_num}')
print(f'Количество букв без отверстий: {len(raw_text) - holes_num}')

print(hole_words)
