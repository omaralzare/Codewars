# https://www.codewars.com/kata/5f70c883e10f9e0001c89673
def flip(d, a):
    a.sort()
    return a if d == "R" else a[::-1]
