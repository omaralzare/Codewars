# https://www.codewars.com/kata/55edaba99da3a9c84000003b
def divisible_by(numbers, divisor):
    newNumbers = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            newNumbers.append(numbers[i])
    return newNumbers
