# https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    result = []
    n = list(str(n))
    n.reverse()
    for i in n:
        result.append(int(i))
    return result


# return [int(x) for x in str(n)[::-1]]
