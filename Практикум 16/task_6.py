def diff_digits(n: int) -> bool:
    """
    Shows if number consists of different digits
    :param n: users number
    :return: True, False
    """
    return len(list(str(n))) == len(set(str(n)))


def solve_hod_mat() -> list:
    """
    Shows all solutions for equation: HOD + HOD + HOD = MAT
    :return: solutions
    """
    hod = set(i for i in range(100, 334) if diff_digits(i))
    hod_mat = []

    for num in hod:
        if not set(str(num * 3)) & set(str(num)):
            hod_mat.append((num, num * 3))

    return hod_mat


def main() -> None:
    for solution in solve_hod_mat():
        hod = solution[0]
        mat = solution[1]
        print(f'{hod}+{hod}+{hod}={mat}')


if __name__ == '__main__':
    main()



