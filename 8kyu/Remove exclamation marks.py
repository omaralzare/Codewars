# https://www.codewars.com/kata/57a0885cbb9944e24c00008e
def remove_exclamation_marks(s):
    newS = ""
    for i in range(len(s)):
        if s[i] != "!":
            newS += s[i]
    return newS
