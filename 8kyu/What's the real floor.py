# https://www.codewars.com/kata/574b3b1599d8f897470018f6
def get_real_floor(n):
    return n - 1 if 0 < n < 13 else (n if n <= 0 else n - 2)
