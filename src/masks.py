from typing import Union


def get_mask_card_number(line_1: Union[str]) -> Union[str]:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    slice_1 = line_1[0:3]
    slice_2 = line_1[4:5]
    slice_3 = line_1[-4:]
    return slice_1 + " " + slice_2 + "** **** " + slice_3


def get_mask_account(line_2: Union[str]) -> Union[str]:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    slice_1 = line_2[-4:]
    return "**" + slice_1
