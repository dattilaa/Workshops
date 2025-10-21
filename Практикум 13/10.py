def print_certain_num(a, b):
    if a > b:
        a, b = b, a
    digits = [1, 3, 4, 8, 9]

    for i in range(a, b + 1):
        k = 0
        for j in str(i):
            if int(j) in digits:
                k += 1
        if k == len(str(i)):
            print(i)


first_num, last_num = map(int, input().split())
print(print_certain_num(first_num, last_num))