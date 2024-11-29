# https://www.codewars.com/kata/51c8991dee245d7ddf00000e
def reverse_words(s):
    s = s.split()[::-1]
    result = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            result += s[i]
        else:
            result += s[i] + " "
    return result
