import json
import datetime


def latests_operations(file_json, num_op=5) -> list:
    """
    returns a list of the specified number of dictionaries from a list of dictionaries sorted by value
    :param file_json: json file with
    :param num_op: int: number of returned dictionaries
    :return: list dicts sorted list by parameter < num_op:> will return the last by parameter <num_op>
    """
    with open(file=file_json, mode="r", encoding="UTF-8") as f:
        data = json.load(f)
        data_filter = filter(lambda x: x.get("state") == "EXECUTED", data)  # фильтр списка словарей по значению
        data_sort = sorted(data_filter, key=lambda x: x["date"], reverse=True)  # сортировка списка словарей по ключу
        data_last_oper = data_sort[:num_op]  # срез последних значений (словарей) в запрашиваемом количестве
        return data_last_oper  # возвращает список по (фильтр словарей->сортировка словарей->количество последних словарей)


def print_operations(data: list):
    """
    prints the specified list of dictionaries sorted by value
    :param data: list: list of dictionaries
    :return: prints
    """

    def prt(key):
        return get_val(data, key) # возвращает значение по ключу
    #вывод на печать
    return (f"{format_date(prt("date"))} {prt("description")}\n"
            f"{format_number(prt("from"), "from")} -> {format_number(prt("to"), "to")}\n"
            f"{prt("amount")} {prt("code")}\n")


def get_val(data, key) -> str:
    """
    searching for a value in a dictionary by key
    :param data: list: list of dictionaries
    :param keys: str: key to search
    :return: value:
    """
    if key in data: # поиск ключа на первом уровне
        return data[key] # ключ найден выше, возвращем значение по найденому ключу, прерываем выполнение функции
    for k, v in data.items(): # перебираем ключ/значение в словаре
        if isinstance(v, dict): # если значение это словарь то...
            item = get_val(v, key) # вызываем эту же функцию, но уже с параметром data = v (словарь)
            if item is not None:
                return item
            else:
                return ""


def format_number(data, tp) -> str:
    """
    masking the meaning
    :param data: str: string to be mined
    :param tp: str: sort key
    :return: str: misc value
    """
    try:
        val_num: str = data.rsplit(" ", 1)
        val, num = val_num[0], val_num[1]
        mask_length = len(num) - 10
        num = num[:6] + "*" * mask_length + num[-4:]
    except IndexError:
        return ""
    if tp in "from":
        res, x, y = "", 0, 4
        while y <= len(num):
            res += " " + num[x: y]
            x, y = x + 4, y + 4
    elif tp in "to":
        res = " " + num[-6:]
    return val + res


def format_date(data) -> str:
    """
    formatting the date
    :param data: str: date in the format YYYY-mm-ddTHH:MM:SS.fffff
    :return: str: date in the format dd.mm.YYYY
    """
    data = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    format_date = "%d.%m.%Y"
    return data.strftime(format_date)


