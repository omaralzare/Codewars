# https://www.codewars.com/kata/57eae65a4321032ce000002d
def fake_bin(x):
    binary = ""
    for i in range(len(x)):
        if int(x[i]) < 5:
            binary += "0"
        else:
            binary += "1"
    return binary
