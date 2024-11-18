# https://www.codewars.com/kata/5513795bd3fafb56c200049e
def count_by(x, n):
    y = x
    arr = []
    for i in range (0,n):
        arr.append(y)
        y += x
    return arr
