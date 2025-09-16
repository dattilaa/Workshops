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
