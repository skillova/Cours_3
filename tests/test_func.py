import func


def test_get_val():
    assert func.get_val({"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
                         "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                         "description": "Открытие вклада", "from": "Visa Classic 2842878893689012",
                         "to": "Счет 90424923579946435907"}, "id") == 863064926
    assert func.get_val({"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
                         "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                         "description": "Открытие вклада",
                         "to": "Счет 90424923579946435907"}, "from") == ""


def test_format_number():
    assert func.format_number("Visa Classic 2842878893689012", 'from') == "Visa Classic 2842 87** **** 9012"
    assert func.format_number("Счет 90424923579946435907", 'from') == "Счет 9042 49** **** **** 5907"
    assert func.format_number("Счет 90424923579946435907", 'to') == "Счет **5907"
    assert func.format_number("", 'from') == ""


def test_format_date():
    assert func.format_date("2019-12-08T22:46:21.935582") == "08.12.2019"


def test_print_operations():
    assert func.print_operations({'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                   'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                                   'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}) == ('08.12.2019 Открытие вклада\n -> Счет **5907\n41096.24 USD\n')
