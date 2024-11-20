# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
def invert(lst):
    newLst = []
    for i in range(len(lst)):
        newLst.append(-lst[i])
    return newLst
