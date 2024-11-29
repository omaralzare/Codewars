# https://www.codewars.com/kata/5951d30ce99cf2467e000013
def pythagorean_triple(integers):
    return (
        integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2
        or integers[1] ** 2 + integers[2] ** 2 == integers[0] ** 2
        or integers[0] ** 2 + integers[2] ** 2 == integers[1] ** 2
    )
