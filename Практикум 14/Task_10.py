list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
b1, b2 = map(int, input().split())

range_nums = reversed(list_1[b1 - 1:b2 + 1])
for i in range_nums:
    list_1.remove(i)
    list_2.append(i)

print(list_1, list_2, sep='\n')
