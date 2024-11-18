#https://www.codewars.com/kata/583710ccaa6717322c000105/python
def simple_multiplication(number) :
    if number % 2 == 0:
        number = number * 8
        return number
    else:
        number = number * 9
        return number
