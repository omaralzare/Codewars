# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
def is_uppercase(inp):
    check = True
    for i in inp:
        if i.islower():
            check = False
    return check
