def communication_cost() -> int:
    card_prices = [5, 10, 25, 50, 100]
    while (card_price := int(input())) not in card_prices:
        continue
    match card_price:
        case 25:
            card_price += 3
        case 50:
            card_price += 8
        case 100:
            card_price += 20
    return card_price

print(communication_cost())

