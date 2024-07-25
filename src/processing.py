import os
from typing import Any

info_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(info_data: list[dict[str, Any]], state_id: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция, описывающая фильтр банкосвких операций по ключу id"""
    new_list = []
    for key in info_data:
        if key.get("state") == state_id:
            new_list.append(key)
    return new_list


print(filter_by_state(info_data))


def sort_by_date(info_data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки данных по дате"""
    sorted_list = sorted(info_data, key=lambda info_data: info_data["date"], reverse=reverse)
    return sorted_list


print(sort_by_date(info_data))
