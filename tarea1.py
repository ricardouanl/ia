def cubo(number):
    return number * number * number

def factorial(number):
    if number == 0:
        return 1
    res = 1
    while number > 1:
        res = res * number
        number -= 1
    return res

def cuenta_patron(patron, cadena):
    if len(patron) == 0 or len(cadena) == 0:
        return 0
    matches = 0
    start_at = 0
    patron_array = list(patron)
    cadena_array = list(cadena)
    while True:
        index = 0
        cadena_array = cadena_array[start_at:]
        #print(cadena_array)
        for char in cadena_array:
            if char != patron_array.pop(0):
                patron_array = list(patron)
                #print(1)
            else:
                if len(patron_array) == 0:
                    matches += 1
                    patron_array = list(patron)
                    index += 1
                    start_at = index - len(patron) + 1
                    break
            index += 1
        if index == len(cadena_array):
            break
    return matches

