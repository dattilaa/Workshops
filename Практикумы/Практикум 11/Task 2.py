# Task 2
line = input()
counter = 0
max_count = 0

for i in range(1, len(line)):
    if line[i] == line[i-1]:
        counter += 1
    else:
        if counter > max_count:
            max_count, counter = counter, 0

print(max_count)
