# Task 6
text = input()
for i in range(len(text) - 1, 0, -1):
    if i == len(text) - 1:
        print(text[i].upper(), end='')
    else:
        print(text[i], end='')
print(text[0].lower())
