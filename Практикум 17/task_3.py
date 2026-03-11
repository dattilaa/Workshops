def main() -> None:
    antonyms = {}

    for index in range(int(input())):
        word, antonym = input().split()
        antonyms[word.lower()] = antonym.lower()

    users_word = input().lower()
    print(antonyms.get(users_word, users_word))


if __name__ == '__main__':
    main()