def count_price(total_price, holiday, loyalty) -> float:
    percent_discount = 0
    if total_price > 30000:
        percent_discount += 10
    elif 5000 < total_price <= 15000:
        percent_discount += 3
    elif 15000 < total_price <= 20000:
        percent_discount += 5
    elif 20000 < total_price <= 30000:
        percent_discount += 7

    if holiday:
        percent_discount += 3
    if loyalty:
        percent_discount += 5

    discount = percent_discount / 100
    disc_price = total_price * (1 - discount)
    if percent_discount >= 15:
        return round(total_price * 0.85, 2)
    return round(disc_price, 2)

pr = float(input('Введите стоимость покупки: '))
while True:
    try:
        hol= int(input('Является ли сегодняшний день праздничным? (1 - да, 0 - нет) '))
        user_loyalty = int(input('У вас есть дисконтная карта? (1 - да, 0 - нет) '))
        if hol not in [0,1] or user_loyalty not in [0,1]:
            continue
        print(count_price(pr, hol, user_loyalty))
        break
    except ValueError:
        continue

