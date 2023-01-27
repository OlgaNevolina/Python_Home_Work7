from excep import *
from mod_calc import *
from logg import logging

type_dict = {"1": "rational", "2": "complex"}
operator = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "sqrt"}

def menu():
    print("Добро пожаловать в калькулятор!\n")
    while True:
        type_num = input("Введите вид чисел:"
                         "\n1 - rational"
                         "\n2 - complex"
                         "\n3 - exit\n")
        match type_num:
            case "1" | "2":
                menu_calc(type_num)
            case "3":
                logging.info("Остановить программу.")
                print("До свидания!")
                break
            case _:
                logging.warning("Выбрано неверно.")
                print("Попробуйте еще раз!")

def menu_calc(data_type):
    global operator
    logging.info(f"Start menu calc. With {type_dict[data_type]}.")
    first, second = 0, 0
    result = "q"
    sign = "/"
    while True:
        op = input("Введите операцию:"
                   "\n1 - sum"
                   "\n2 - dif"
                   "\n3 - mult"
                   "\n4 - div"
                   "\n5 - pow"
                   "\n6 - sqrt"
                   "\n7 - previous menu\n")

        if op.isdigit() and int(op) in range(1, 6):
            if data_type == "1":
                first, second = check_in([input(f"Введите {i + 1} число ") for i in range(2)], data_type)
            elif data_type == "2":
                first, second = [complex(*check_in([input(f"Введите {i + 1} вещественную часть: "),
                                                    input(f"Введите {i + 1} мнимую часть: ")], data_type, i))
                                 for i in range(2)]
        match op:
            case "1":
                result = sum_data(first, second)
                logging.info(f"Sum: {first} + {second} = {result}")
            case "2":
                result = dif_data(first, second)
                logging.info(f"Dif: {first} - {second} = {result}")
            case "3":
                result = mult_data(first, second)
                logging.info(f"Mult: {first} * {second} = {result}")
            case "4":
                if data_type == "1":
                    second = check_zero_real(str(second))
                    sign = menu_divisions()
                    operator[op] = sign
                else:
                    second = check_zero_comp(first, second)
                    operator[op] = "/"
                if sign:
                    result = div_data(first, second)
                    logging.info(f"Div: {first} {sign} {second} = {result}")
            case "5":
                result = pow_data(first, second)
                logging.info(f"Pow: {first} ^ {second} = {result}")
            case "6":
                second = ""
                if data_type == "1":
                    first = check_in_one([input(f"Введите число: ")], data_type)
                else:
                    first = complex(*check_in_one([input(f"Введите вещественную часть: "),
                                                   input(f"Введите мнимую часть: ")], data_type))
                result = pow_data(first)
                logging.info(f"Sqrt: {first} = {result}")
            case "7":
                logging.info('Стоп')
                print()
                break
            case _:
                logging.warning(f"Выбрано неверно.")
                print("Ошибка. Попробуйте еще раз!")
                continue
        if result != "q":
            print(f"Res: {first} {operator[op]} {second} = {result}", end="\n\n")

def menu_divisions():
    logging.info(f"Start menu divisions.")
    while True:
        op = input("Операции:\n"
                   "1 - '/'\n"
                   "2 - '//'\n"
                   "3 - '%'\n"
                   "4 - previous menu\n")
        match op:
            case "1":
                return "/"
            case "2":
                return "//"
            case "3":
                return "%"
            case "4":
                logging.info('Стоп')
                print()
                return 0
            case _:
                logging.warning(f"Выбрано неверно.")
                print("Ошибка. Попробуйте еще раз!")
                                   
