# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e
def sum_of_differences(arr):
    sum = 0
    if arr:
        arr.sort()
        arr.reverse()
        for i in range(len(arr) - 1):
            sum += arr[i] - arr[i + 1]
        return sum
    else:
        return sum
