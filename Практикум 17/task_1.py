def count_sort(words: dict) -> dict:
    """
    Sorting dict by words frequency in reverse
    :param words: users dict
    :return: sorted dict
    """
    return dict(sorted(words.items(), reverse=True))


def main() -> None:
    words = list(input().split())
    freq_dict = {word: words.count(word) for word in words}

    for word in count_sort(freq_dict).keys():
        print(word)


if __name__ == '__main__':
    main()


