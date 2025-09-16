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

