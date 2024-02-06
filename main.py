from func import get_file, selection_of_operations, get_val, format_date, mask_number
import pathlib

file_json = pathlib.Path.cwd() / "data" / "operations.json"


def main(data, num=5):
    operations_all = get_file(data)
    last_operations = selection_of_operations(operations_all, num)
    for operation in last_operations:
        items = {'date': '', 'description': '', 'from': '', 'to': '', 'amount': '', 'code': ''}
        for key in items:
            val = get_val(operation, key)
            items[key] = val
        print(f"{format_date(items['date'])} {items['description']}\n"
              f"{mask_number(items['from'])} -> {mask_number(items['to'])}\n"
              f"{items['amount']} {items['code']}\n")


if __name__ == "__main__":
    main(file_json)
