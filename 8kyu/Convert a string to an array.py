# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
def string_to_array(s):
    if s == "":
        return [s]
    else:
        return s.split()
