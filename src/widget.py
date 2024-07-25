from src.masks import get_mask_card_number, get_mask_account
def mask_account_card(input_data: str) -> str | None:
    """Функция маскировки карты или счета"""

    if "Счет" in input_data:
        return get_mask_account(input_data)
    else:
        return get_mask_card_number(input_data)

def get_date(input_data: str) -> str | None:
    """Функция преобразования даты"""
    date = input_data.split("T")[0]
    slice_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"

    return slice_date


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

