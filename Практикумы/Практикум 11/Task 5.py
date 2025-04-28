f = open('input.txt', 'r', encoding='utf-8')
o = open('output.txt', 'w', encoding='utf-8')
num_list = []
try:
    for line in f:
        num = float(line)
        num_list.append(num)
    o.write(str(num_list[0] / num_list[1] + num_list[2]))
except ZeroDivisionError:
    o.write('Division by zero')
except ValueError:
    o.write('Data error')