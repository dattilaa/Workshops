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
