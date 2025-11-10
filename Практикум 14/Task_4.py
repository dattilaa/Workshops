import re

text = input('Введите предложение: ')
words = re.findall(r'\b\w+\b', text.lower())

print(set(words))