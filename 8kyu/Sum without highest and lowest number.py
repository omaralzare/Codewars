# https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    sum = 0
    if arr:
        if len(arr) != 1:
            for i in range(len(arr)):
                sum += arr[i]
            return sum - max(arr) - min(arr)
        else:
            return 0
    else:
        return 0
