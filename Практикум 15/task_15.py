def ten_to_bin(x: int) -> str:
    """
    function, converting number from decimal to binary number system
    :param x: users number
    :return: binary_number
    """
    match x:
        case 0:
            return '0'
        case 1:
            return '1'

    return ten_to_bin(x // 2) + str(x % 2)


print(ten_to_bin(375))