# https://www.codewars.com/kata/568d0dd208ee69389d000016
def rental_car_cost(d):
    return d * 40 if d < 3 else (d * 40 - 20 if d >= 3 and d < 7 else d * 40 - 50)
