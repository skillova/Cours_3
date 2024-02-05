from func import latests_operations, print_operations
import pathlib

file_json = pathlib.Path.cwd() / "data" / "operations.json"


def main(data, num):
    last_opers = latests_operations(data, num)
    for data in last_opers:
        print(print_operations(data))


if __name__ == "__main__":
    main(file_json, 5)
