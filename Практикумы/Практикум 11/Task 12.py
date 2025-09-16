import keyword as kw

alphabet = [chr(i) for i in range(97, 123)]
nums = [str(i) for i in range(10)]
print(nums)
symbols = alphabet + nums
symbols.append('_')
name = input()

if not kw.iskeyword(name) and name[0] not in nums:
    print(name[0])
    flag = True
    for i in name[1:]:
        if i not in symbols:
            flag = False
            print('Не может быть именем')
            break
    if flag:
        print('Может быть именем')
else:
    print('Не может быть именем')
