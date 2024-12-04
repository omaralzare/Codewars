# https://www.codewars.com/kata/57cff961eca260b71900008f
def is_vow(inp):
    check = ["a", "e", "i", "o", "u"]
    for i in range(len(inp)):
        if chr(inp[i]) in check:
            inp[i] = chr(inp[i])
    return inp
