# https://www.codewars.com/kata/56b29582461215098d00000f
def pipe_fix(nums):
    nums.sort()
    result = []
    for i in range(nums[0], nums[-1] + 1):
        result.append(i)
    return result
