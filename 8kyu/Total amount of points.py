# https://www.codewars.com/kata/5bb904724c47249b10000131
def points(games):
    score = 0
    for i in range(10):
        if games[i][0] > games[i][2]:
            score += 3
        elif games[i][0] == games[i][2]:
            score += 1
    return score
