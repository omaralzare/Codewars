# https://www.codewars.com/kata/5aa736a455f906981800360d
def feast(beast, dish):
    return True if (dish.startswith(beast[0]) and dish.endswith(beast[-1])) else False
