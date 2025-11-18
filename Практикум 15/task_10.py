def maxlist(user_list: list) -> int:
    """
    function, returning max element from int list
    :param user_list: user num list
    :return: max num
    """
    match len(user_list):
        case 1:
            return user_list[0]
    return user_list[0] if user_list[0] > maxlist(user_list[1:]) \
        else maxlist(user_list[1:])






