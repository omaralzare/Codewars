# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
def past(h, m, s):
    # h = 3600000 ms
    # m = 60000 ms
    # s = 1000 ms
    return (h * 3600000) + (m * 60000) + (s * 1000)
