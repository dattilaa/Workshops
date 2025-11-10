import re


seq_words = {}
order = 0

while text := input():
    order += 1
    raw_text = re.sub(r'[^\w\s]', '', text.lower())
    counter = 1
    if raw_text in seq_words.keys():
        counter = seq_words.get(raw_text)[0]
        counter += 1
        order = seq_words.get(raw_text)[1]
    seq_words[raw_text] = (counter, order)

sorted_words = sorted(seq_words.items(), key=lambda x: (-x[1][0], x[1][1]))
for item in sorted_words:
    print(item[0])



