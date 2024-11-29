# https://www.codewars.com/kata/586c1cf4b98de0399300001d
def combat(health, damage):
    return health - damage if (health - damage) > 0 else 0
