# https://www.codewars.com/kata/58649884a1659ed6cb000072
def update_light(current):
    return "green" if current == "red" else ("red" if current == "yellow" else "yellow")
