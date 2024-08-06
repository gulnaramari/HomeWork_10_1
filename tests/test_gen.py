import pytest
from typing import Generator, Any
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
            "description": "Translated from organization",
            "from": "Account 75106830613657916952",
            "to": "Account 11776614605963066702"
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
            "description": "Transfer from account to account",
            "from": "Account 19708645243227258542",
            "to": "Account 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Transfer from account to account",
            "from": "Account 44812258784861134719",
            "to": "Account 74489636417521191160"
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
            "description": "Transfer from one card to another",
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
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Translated from organization",
            "from": "Visa Platinum 1246377376343588",
            "to": "Account 14211924144426031657"
        }
    ]
)


def test_filter_by_currency(transactions: list,
                       valuta_code: str = "USD") -> Generator[Any, Any, Any]:
    generator = filter_by_currency(transactions)
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Translated from organization",
            "from": "Account 75106830613657916952",
            "to": "Account 11776614605963066702"
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
            "description": "Transfer from account to account",
            "from": "Account 19708645243227258542",
            "to": "Account 75651667383060284188"
        }


def test_transaction_descriptions():
    a = transaction_descriptions(transactions)
    assert next(a) == "Translated from organization"


@pytest.mark.parametrize("index, expected", [
    (1, "Transfer from account to account"), (3, "Transfer from one card to another")
])
def test_transaction_descriptions_index(index, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    num = card_number_generator(800, 801)
    assert next(num) == "0000 0000 0000 0800"


def test_card_number_generator_ending():
    num = card_number_generator(9999999999999998, 9999999999999999)
    assert next(num) == "9999 9999 9999 9998"
    assert next(num) == "9999 9999 9999 9999"


def test_card_number_generator_begin():
    numer = card_number_generator(1, 2)
    assert next(numer) == '0000 0000 0000 0001'
