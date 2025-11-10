nums = list(map(int, input().split()))
even_sum, odd_sum = 0, 0

for num in nums:
    if num % 2:
        odd_sum += num
        continue
    even_sum += num

print(f'Сумма четных элементов: {even_sum}\n'
      f'Сумма нечетных элементов: {odd_sum}',)