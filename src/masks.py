def get_mask_card_number(input_data: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    new_cardnumber = ""
    new_cardname = ""
    if "Visa Platinum" or "MasterCard" or "Maestro" in input_data:
        for symbol in input_data:
            if symbol.isdigit():
                new_cardnumber += symbol
            elif symbol.isalpha():
                new_cardname += symbol

        if len(new_cardnumber) == 16:
            """Случай нестандартной длины номера карты"""
            slice_1 = new_cardnumber[0:4]
            slice_2 = new_cardnumber[4:6]
            slice_3 = new_cardnumber[-4:]
            mask_card = slice_1 + " " + slice_2 + "** **** " + slice_3
        else:
            print("Неверный формат данных")

    return (f"{new_cardname} {mask_card}")


def get_mask_account(input_data: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    new_number = ""
    new_name = ""
    if "Счет" in input_data:
        for symbol in input_data:
            if symbol.isalpha():
                new_name += symbol
            elif symbol.isdigit():
                new_number += symbol
    slice_number = new_number[-4:]
    mask_account = "**" + slice_number
    return (f"{new_name} {mask_account}")
