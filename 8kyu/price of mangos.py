# https://www.codewars.com/kata/57a77726bb9944d000000b06/
def mango(quantity, price):
    counterPrice = 0
    finalPrice = 0
    for i in range(1, quantity + 1):
        counterPrice += 1
        if counterPrice == 3:
            counterPrice = 0
            continue
        finalPrice += price
    return finalPrice
