# https://www.codewars.com/kata/56efc695740d30f963000557
def to_alternating_case(string):
    newString = ""
    for i in range(len(string)):
        if string[i].isupper():
            newString += string[i].lower()
        else:
            newString += string[i].upper()
    return newString
