import json
import datetime


def get_file(file_json) -> list:
    with open(file=file_json, mode="r", encoding="UTF-8") as file:
        data_operations = json.load(file)
        return data_operations


def selection_of_operations(list_operations, quantity=5) -> list:
    """
    returns a list of the specified number of dictionaries from a list of dictionaries sorted by value
    """
    operations_filter = filter(lambda x: x.get("state") == "EXECUTED",
                               list_operations)  # фильтр списка словарей по значению
    operations_sort = sorted(operations_filter, key=lambda x: x["date"],
                             reverse=True)  # сортировка списка словарей по ключу
    last_operations = operations_sort[:quantity]  # срез последних значений (словарей) в запрашиваемом количестве
    return last_operations  # возвращает список (фильтр словарей->сортировка словарей->количество последних словарей)


def get_val(data, key) -> str:
    """
    searching for a value in a dictionary by key
    """
    if key in data:  # поиск ключа на первом уровне
        return data[key]  # ключ найден выше, возвращем значение по найденому ключу, прерываем выполнение функции
    for k, v in data.items():  # перебираем ключ/значение в словаре
        if isinstance(v, dict):  # если значение это словарь то...
            item = get_val(v, key)  # вызываем эту же функцию, но уже с параметром data = v (словарь)
            if item is not None:
                return item
            else:
                return ""


def mask_number(line_with_number) -> str:
    """
    masking the meaning
    """
    try:
        line_with_number = line_with_number.split()
        number = line_with_number[-1]
    except IndexError:
        return ''
    if str(line_with_number).startswith('Счет'):
        number = f'**{number[-4:]}'
    else:
        number = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    line_with_number[-1] = number
    return ' '.join(line_with_number)


def format_date(data) -> str:
    """
    formatting the date
    """
    data = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    form_date = "%d.%m.%Y"
    return data.strftime(form_date)
