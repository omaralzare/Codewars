# https://www.codewars.com/kata/5b853229cfde412a470000d0
def twice_as_old(dad_years_old, son_years_old):
    return (
        dad_years_old - (son_years_old * 2)
        if dad_years_old >= son_years_old * 2
        else (son_years_old * 2) - dad_years_old
    )
