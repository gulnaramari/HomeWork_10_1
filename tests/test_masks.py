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
def test_get_mask_card_number(input_data: str, expected_mask: str) -> str:
    assert get_mask_card_number(input_data) == expected_mask
