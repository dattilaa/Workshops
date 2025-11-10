def sum_list(a) -> list:
    """
    function, returning list with sums of numbers standing next to each other
    :param a: list
    :return: new_list
    """
    new_list = []
    for i in range(1, len(a) - 1):
        new_list.append(a[i - 1] + a[i])
    return new_list

based_list = []
for j in range(10):
    n = int(input())
    based_list.append(n)

print(sum_list(based_list))
