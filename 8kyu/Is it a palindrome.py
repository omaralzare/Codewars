# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
def is_palindrome(s):
    check = True
    for i in range(len(s) // 2):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            check = False
    return check
