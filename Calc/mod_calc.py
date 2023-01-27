def sum_data(first_number, second_number):
    return first_number + second_number

def dif_data(first_number, second_number):
    return first_number - second_number 

def mult_data(first_number, second_number):
    return first_number * second_number

def div_data(first_number, second_number, par = '/'):
    if par == '%':
        return round(first_number % second_number, 2)
    elif par == '//':
        return first_number // second_number
    return first_number / second_number

def pow_data(first_number, second_number = None):
    if not second_number:
        return first_number ** 0.5
    return first_number ** second_number                  