def find_substring(text, substr) -> int:
    unique_chars = set()
    substr_len = len(substr)
    offsets = {}

    for i in range(substr_len - 2, -1, -1):
        if substr[i] not in unique_chars:
            offsets[substr[i]] = substr_len - i - 1
            unique_chars.add(substr[i])

    if substr[substr_len - 1] not in unique_chars:
        offsets[substr[substr_len - 1]] = substr_len

    offsets['*'] = substr_len

    text_len = len(text)

    if text_len >= substr_len:
        i = substr_len - 1

        while i < text_len:
            k = 0
            flag = False
            for j in range(substr_len - 1, -1, -1):
                if text[i - k] != substr[j]:
                    if j == substr_len - 1:
                        offset = offsets[text[i]] if offsets.get(text[i], False) else offsets['*']
                    else:
                        offset = offsets[substr[j]]

                    i += offset
                    flag = True
                    break

                k += 1

            if not flag:
                return i - k + 1
        else:
            return -1

    else:
        return -1


def all_substring_enters(text, substr) -> list:
    indices = []
    start = 0

    while start <= len(text) - len(substr):
        pos = find_substring(text[start:], substr)
        if pos == -1:
            break

        actual_pos = start + pos
        indices.append(actual_pos)
        start = actual_pos + 1

    return indices


print(all_substring_enters('ATGGGATGGACATGACTACCGATGCGGGATTGGCGAG', 'ATGG'))
