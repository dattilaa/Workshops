import json

def main() -> None:
    json_input = '[["hello", 10], ["world", 20], ["python", 30]]'
    data = json.loads(json_input)

    print(sorted(data, key=lambda x: -x[1]))


if __name__ == '__main__':
    main()

