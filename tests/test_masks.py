import os

import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def input_data() -> list[str]:
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 7000892289606361",
        "Maestro 6769070082797565",
        "MasterCard 6700000082797565"
    ]


@pytest.mark.parametrize("input_data, expected_mask", [
                        ("Visa Platinum 7000792289606361", "VisaPlatinum 7000 79** **** 6361"),
                        ("Maestro 7000892289606361", "Maestro 7000 89** **** 6361"),
                        ("Maestro 6769070082797565", "Maestro 6769 07** **** 7565"),
                        ("MasterCard 6700000082797565", "MasterCard 6700 00** **** 7565"),
])
def test_get_mask_card_number(input_data: str, expected_mask: str) -> str | None:
    assert get_mask_card_number(input_data) == expected_mask


def test_get_invalid_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("12345678")


def test_get_invalid_name_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("12opyu3456kljh78")


def test_short_get_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("1")


def test_get_empty_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("Hello")


def test_get_none_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_null_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("0")


def test_get_format_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("*")


def test_get_upper_format_name_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("VISA")
