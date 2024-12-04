# https://www.codewars.com/kata/5b4e779c578c6a898e0005c5
def draw_stairs(n):
    output = ""
    for i in range(n):
        if i == n - 1:
            output += "I"
        else:
            output += "I\n" + " " * (i + 1)
    return output
