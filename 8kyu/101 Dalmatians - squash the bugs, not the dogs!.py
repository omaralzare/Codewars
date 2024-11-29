# https://www.codewars.com/kata/56f6919a6b88de18ff000b36
def how_many_dalmatians(n):
    dogs = [
        "Hardly any",
        "More than a handful!",
        "Woah that's a lot of dogs!",
        "101 DALMATIONS!!!",
    ]
    if n <= 10:
        respond = dogs[0]
    elif 10 < n <= 50:
        respond = dogs[1]
    elif 50 < n <= 100:
        respond = dogs[2]
    else:
        respond = dogs[3]
    return respond
