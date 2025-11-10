def find_three(nums: list) -> bool:
    """
    function, showing if three enters the list only once
    :param nums: user list
    :return: True, False
    """
    if nums.count(3) != 1:
        return False
    return True


while not find_three(user_list := list(map(int, input().split()))):
    print('В списке помимо других чисел должна быть ОДНА тройка!')

user_list.remove(3)
print(user_list)