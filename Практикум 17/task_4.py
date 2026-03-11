import ru_local as ru


def main() -> None:
    shapes = {}

    for index in range(int(input())):
        objects = list(input().split())
        shapes[objects[0]] = objects[1:]

    user_word = input()
    for shape in shapes.keys():
        if user_word in shapes[shape]:
            print(shape)

            return None


    print(ru.UNKNOWN)


if __name__ == '__main__':
    main()
