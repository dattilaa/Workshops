def check_command(command: str) -> bool:
    """
    function, checking if command is written correctly
    :param command: user command
    :return: True, False
    """
    try:
        int(command[1:])
    except ValueError:
        return False
    if command[0].lower() in ['r', 'l']:
        return True
    return False


def shift_by(user_list: list, command: str) -> list:
    """
    function, shifting elements of list in direction ordered by user
    :param user_list: input list
    :param command: input command that shows direction of shifting
    and number of changes
    :return: shifted list
    """
    direction, amount = command[0].lower(), int(command[1:]) % len(user_list)
    shifts, new_list = [], []
    match direction:
        case 'r':
            shifts = user_list[amount - 1:]
        case 'l':
            shifts = user_list[amount:]

    for num in shifts:
        user_list.remove(num)

    return shifts + user_list

my_list = list(map(int, input().split()))
while not check_command(my_command := input()):
    continue

print(shift_by(my_list, my_command))

