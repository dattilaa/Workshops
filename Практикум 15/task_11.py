def ind_maxlist(user_list: list) -> int:
    """
    function, finding index of max element in list
    :param user_list: user list
    :return: max_el_index
    """
    match len(user_list):
        case 1:
            return 0
    
    start_index = 0
    sub_index = ind_maxlist(user_list[1:]) + 1

    if user_list[start_index] > user_list[ind_maxlist(user_list[1:])]:
        return start_index
    else:
        return sub_index




list_1 = [1, 2, 6, 3, 4]
print(ind_maxlist(list_1))