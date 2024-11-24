# https://www.codewars.com/kata/5547929140907378f9000039
def shortcut(s):
    newS = ""
    for i in range(len(s)):
        if s[i] not in "aeiou":
            newS += s[i]
    return newS
