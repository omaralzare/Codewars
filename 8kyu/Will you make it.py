# https://www.codewars.com/kata/5861d28f124b35723e00005e
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (mpg * fuel_left) >= distance_to_pump else False
