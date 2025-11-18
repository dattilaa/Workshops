def search(user_list: list, x: int) -> int:
    """
    function, showing if user list contains x
    :param user_list: users num list
    :param x: desirable element
    :return: 1, 0
    """
    match len(user_list):
        case 0:
            return 0

    return 1 if user_list[0] == x else search(user_list[1:], x)



