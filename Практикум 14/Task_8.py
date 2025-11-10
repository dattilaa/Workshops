def sorted_str(text: str) -> str:
    """
    function, returning new string made from sorted chars of previous text
    :param text: user text
    :return: sorted_text
    """
    chars = [char for char in text.lower()]
    sorted_chars = sorted(chars)

    return ''.join(sorted_chars)

print(sorted_str(input()))