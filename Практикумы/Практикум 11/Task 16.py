def check_chars(text):
    chars = []
    for s in text:
        if s == '(':
            chars.append(s)
        elif s == ')':
            if not chars:
                return False
            chars.pop()

    return not len(chars)

print(check_chars(input()))
