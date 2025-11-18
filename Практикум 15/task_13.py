def odd_list(user_list: list, n: int) -> list:
    """
    function, returning list with odd nums from users input
    :param user_list: users list
    :param n: length of list
    :return: odd_list
    """
    match n:
        case 0:
            return []

    if not user_list[n - 1] % 2:
        return [user_list[n - 1]] + odd_list(user_list, n - 1)
    return odd_list(user_list, n - 1)



list_1 = [1, 2, 3, 4, 5, 6]
print(odd_list(list_1, len(list_1)))