def mask_account_card(input_data: str) -> str | None:
    """Функция маскировки карты или счета"""

    if "Счет" in input_data:
        return get_mask_account(input_data)
    else:
        return get_mask_card_number(input_data)

def get_data(input_data: str) -> str | None:
    """Функция преобразования даты"""
    data = input_data.split("T")[0]
    slice_data = f"{data[-2:]}.{data[5:7]}.{data[:4]}"

    return slice_data


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_data("2024-03-11T02:26:18.671407"))
