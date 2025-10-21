def make_payment(p):
    if p < 20 or p > 1000:
        print('Повторить попытку')
    else:
        print('Успех')

make_payment(30)