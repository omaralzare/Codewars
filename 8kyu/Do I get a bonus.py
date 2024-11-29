# https://www.codewars.com/kata/56f6ad906b88de513f000d96
def bonus_time(salary, bonus):
    return (
        f"${salary*10}".format(salary=salary)
        if bonus
        else f"${salary}".format(salary=salary)
    )


# return "${}".format(salary * (10 if bonus else 1))
