def count_courses(n: int) -> int:
    """
    function, showing number of chosen courses
    :param n: number of students
    :return: number of courses
    """
    choice = set()

    for student in range(n):
        courses = input().split()
        for course in courses:
            choice.add(course)

    return len(choice)


def main() -> None:
    print(count_courses(int(input())))


if __name__ == '__main__':
    main()
