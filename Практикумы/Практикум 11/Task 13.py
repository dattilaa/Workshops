# Task 13
def lucky(n):
    if len(n) % 2:
        return False
    s1, s2 = 0, 0
    for i in range(len(n)):
        if i < 3:
            s1 += int(n[i])
        else:
            s2 += int(n[i])
    return True if s1 == s2 else False

counter = 1
while not lucky(num := str(int(input()))):
    counter += 1

print(counter)
