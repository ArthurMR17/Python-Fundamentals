def calculate_tip(bill_amount, tipPercentage):
    tip = bill_amount * tipPercentage / 100
    return round(tip, 2)

    # Tu código aquí 👈
    pass


print(calculate_tip(1524.33, 25))
