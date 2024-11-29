# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    posCounter = 0
    sumNeg = 0
    for i in arr:
        if i > 0:
            posCounter += 1
        elif i < 0:
            sumNeg += i
    return [posCounter, sumNeg] if arr else []
