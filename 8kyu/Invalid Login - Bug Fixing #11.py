# https://www.codewars.com/kata/55e4c52ad58df7509c00007e
def validate(username, password):
    database = Database()
    return database.login(username, password)
