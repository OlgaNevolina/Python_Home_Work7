from typing import Union
from logg import logging

def check_in(data: list, count: str, real_im=0):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        else:
            logging.warning(f"Введено неверно: '{data[0]}', '{data[1]}'!")
            print(f"\n{'*' * 30}\n{'Попробуйте еще!':^30}\n{'*' * 30}\n")
            match count:
                case "1":
                    data = [input(f"Введите {i + 1} число: ") for i in range(2)]
                case "2":
                    match real_im:
                        case 0:
                            data = [input(f"Введите 1 вещественную часть: "), input(f"Введите 1 мнимую часть: ")]
                        case 1:
                            data = [input(f"Введите 2 вещественную часть: "), input(f"Введите 2 мнимую часть: ")]

def check_in_one(data: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        match count:
            case "1":
                if len(check) == 1:
                    return check[0]
                print(f"\n{'*' * 30}\n{'Попробуйте еще!':^30}\n{'*' * 30}\n")
                logging.warning(f"Введено неверно: '{data[0]}'!")
                data = [input(f"Введите число: ")]
            case "2":
                if len(check) == 2:
                    return check
                print(f"\n{'*' * 30}\n{'Попробуйте еще!':^30}\n{'*' * 30}\n")
                logging.warning(f"Введено неверно: '{data[0]}', '{data[1]}'!")
                data = [input(f"Введите вещественную часть: "), input(f"Введите мнимую часть: ")]

def check_zero_real(data: str):
    while True:
        d = [float(i) if "." in i else int(i) for i in [data] if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not (d and d[0]):
            print(f"\n{'*' * 50}\n{'Делить на ноль нельзя! Попробуйте еще!':^50}\n{'*' * 50}\n")
            logging.warning(f"Введено неверно: '{data}'!")
            data = input(f"Введите 2 число: ")
        else:
            return d[0]

def check_zero_comp(data_1: Union[int, float], data_2: Union[int, float]):
    while True:
        try:
            data_1 / data_2
        except ZeroDivisionError:
            print(f"\n{'*' * 50}\n{'Делить на ноль нельзя! Попробуйте еще!':^50}\n{'*' * 50}\n")
            logging.warning(f"Введено неверно: '{data_2}'!")
            data_2 = complex(*check_in([input(f"Введите 2 вещественную часть: "), input(f"Введите 2 мнимую часть: ")], "2", 1))
        else:
            return data_2
