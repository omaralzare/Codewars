# https://www.codewars.com/kata/5a00e05cc374cb34d100000d
def reverse_seq(n):
    result = []
    for i in range(n):
        result.append(n - i)
    return result


# return list(range(n, 0, -1))
