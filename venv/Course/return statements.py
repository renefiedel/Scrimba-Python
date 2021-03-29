def vat(amount):
    tax = amount * 0.25
    tot_amount = amount * 1.25
    # return [amount, tax, tot_amount]
    return f'{amount}, {tax}, {tot_amount}'

price = vat(100)
print(price, type(price))