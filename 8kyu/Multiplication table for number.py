# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
def multi_table(number):
    answer = ""
    for i in range(1, 11):
        result = i * number
        answer += "{i} * {number} = {result}".format(i=i, number=number, result=result)
        if i != 10:
            answer += "\n"
    return answer
