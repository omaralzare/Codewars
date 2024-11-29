# https://www.codewars.com/kata/5966e33c4e686b508700002d
def sum_str(a, b):
    if a != "" and b != "":
        return str(int(a) + int(b))
    elif a == "" and b != "":
        return str(int(b))
    elif b == "" and a != "":
        return str(int(a))
    else:
        return "0"

    # return str(int('0' + a) + int('0' + b))

    # if a == "" or a == None: a = "0"
    # if b == "" or b == None:
    #    b = "0"
    # return str(int(a) + int(b))
