def translate(sentence: list[str], translations: dict) -> str:
    """
    Translates users sentence. If word is not in translations, it remains the same.
    :param sentence: sentence that is going to be translated
    :param translations: translations dictionary
    :return: translated sentence
    """
    return ' '.join(translations.get(word, word) for word in sentence)


def main() -> None:
    translations = {}

    for index in range(int(input())):
        word, translation = input().split()
        translations[word] = translation

    sentence = list(input().split())
    print(translate(sentence, translations))


if __name__ == '__main__':
    main()




