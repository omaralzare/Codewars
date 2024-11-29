# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
def two_sort(array):
    array.sort()
    result = ""
    for i in range(len(array[0])):
        if i == len(array[0]) - 1:
            result += array[0][i]
        else:
            result += array[0][i] + "***"
    return result
