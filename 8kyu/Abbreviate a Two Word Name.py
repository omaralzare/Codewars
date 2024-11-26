# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
def abbrev_name(name):
    name = name.split(" ")
    name1 = name[0][0].upper()
    name2 = name[1][0].upper()
    return "{name1}.{name2}".format(name1=name1, name2=name2)
