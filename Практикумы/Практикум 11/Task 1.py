# Task 1
line = input()
counter = 0
max_count = 0

for i in line:
    if i == ' ':
        counter += 1
    else:
        if counter > max_count:
            max_count, counter = counter, 0


print(max_count)
