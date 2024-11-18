# https://www.codewars.com/kata/5547929140907378f9000039
def shortcut( s ):
    newS = ""
    for i in range(len(s)):
        if (
            s[i] != 'a'
            and s[i] != "e"
            and s[i] != 'o'
            and s[i] != 'i'
            and s[i] != 'u'):
            newS += s[i]
    return newS
