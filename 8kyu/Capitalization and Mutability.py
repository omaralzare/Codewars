# https://www.codewars.com/kata/595970246c9b8fa0a8000086
def capitalize_word (word : str) -> str:
    newWord = ""
    for i in range (len(word)):
        if i == 0:
            newWord += word[i].upper()
        else:
            newWord += word[i].lower()
    return newWord
