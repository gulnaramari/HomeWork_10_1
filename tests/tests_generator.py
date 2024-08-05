import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def test_filter_by_currency():
    generator = filter_by_currency(transactions)
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }

    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }


def test_filter_by_currency_not_code():
    with pytest.raises(SystemExit, match="Отсутствует такая валюта") as expected:
        generator = filter_by_currency(transactions, 'EU')
        assert next(generator) == expected


def test_filter_by_currency_not_code():
    with pytest.raises(SystemExit, match="Отсутствует такая валюта") as expected:
        generator = filter_by_currency(transactions, '')
        assert next(generator) == expected


def test_transaction_descriptions():
    a = transaction_descriptions(transactions)
    assert next(a) == "Перевод организации"


@pytest.mark.parametrize("index, expected", [
    (1, "Перевод со счета на счет"), (3, "Перевод с карты на карту")
])
def test_transaction_descriptions_index(index, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected




def test_transaction_descriptions_empty():
    with pytest.raises(SystemExit, match="Отсутствуют данные о транзакциях") as expected:
        a = transaction_descriptions([])
        assert next(a) == expected


def test_card_number_generator():
    num = card_number_generator(800, 801)
    assert next(num) == "0000 0000 0000 0800"


def test_card_number_generator_ending():
    num = card_number_generator(9999999999999998, 9999999999999999)
    assert next(num) == "9999 9999 9999 9998"
    assert next(num) == "9999 9999 9999 9999"


def test_card_number_generator_begin():
    numer = card_number_generator(1, 2)
    assert next(numer) == '0000 0000 0000 0001'
