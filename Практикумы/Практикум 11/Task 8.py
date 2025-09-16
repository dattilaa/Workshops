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

