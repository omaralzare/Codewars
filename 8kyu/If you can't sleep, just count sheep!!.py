# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
def count_sheep(n):
    string = ""
    if n == 0:
        return string
    else:
        for i in range(1, n + 1):
            string += "{i} sheep...".format(i=i)
    return string
