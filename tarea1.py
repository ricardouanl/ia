def cubo(number):
    return number * number

def factorial(number):
    if number == 0:
        return 1
    res = 1
    while number > 1:
        res = res * number
        number -= 1
    return res
