from typing import Any

info_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 616064591, "state": "FAILED", "date": "2022-02-24T08:21:33.419441"},
]


def filter_by_state(info_data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, описывающая фильтр банковских операций по ключу state"""
    if not isinstance(state, str):
        raise TypeError("Ошибка типа данных")

    if not state:
        raise ValueError("Введите статус правильно")  # Проверка на статус
    new_list = []
    for key in info_data:
        if key.get("state") == state:
            new_list.append(key)

    return new_list


print(filter_by_state(info_data))  # По умолчанию "EXECUTED"
print(filter_by_state(info_data, "CANCELED"))  # Можно передать другое состояние
print(filter_by_state(info_data, "FAILED"))
print(filter_by_state(info_data, "PENDING"))


def sort_by_date(info_data: list[dict[str, Any]], reverse: bool = False) -> Any:
    """Функция сортировки данных по дате и удаление дубликатов"""
    if not all(isinstance(item, dict) for item in info_data):
        raise TypeError("Ошибка типа данных: все элементы должны быть словарями")

    unique_dates = set()
    unique_elements = []
    for item in info_data:
        if not isinstance("date", str):
            raise TypeError("Ошибка типа данных: все даты должны быть формата str")
        if not "date":
            raise ValueError("Введите дату правильно")
        date = item["date"]
        if date not in unique_dates:
            unique_dates.add(date)
            unique_elements.append(item)

    # Сортировка списка словарей по ключу "date"
    sorted_list = sorted(unique_elements, key=lambda x: x["date"], reverse=reverse)
    return sorted_list


print(sort_by_date(info_data, reverse=False))
print(sort_by_date(info_data, reverse=True))
