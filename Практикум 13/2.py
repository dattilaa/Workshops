def print_n_fibnums(n):
    fib_seq = []
    for i in range(n):
        if i <= 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])

    print(fib_seq)


print_n_fibnums(int(input()))