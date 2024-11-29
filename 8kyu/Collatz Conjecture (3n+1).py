# https://www.codewars.com/kata/577a6e90d48e51c55e000217
def hotpo(n):
    cond = True
    counter = 0
    while n != 1 and n > 0:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        elif n != 1:
            n = 3 * n + 1
            counter += 1
    return counter
