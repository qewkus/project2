import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 **** 6361"),
        ("Счет 73654108430135874305", "Счет 4305"),
        ("MasterCard 7000792289606354", "MasterCard 7000 79 **** 6354"),
    ],
)
def test_mask_account_card(info: str, expected: str) -> None:
    assert mask_account_card(info) == expected


def test_mask_account_card_error() -> None:
    with pytest.raises(ValueError):
        mask_account_card("1")


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-08-16T02:26:18.671407", "16.08.2026"),
        ("2028-01-23T02:26:18.671407", "23.01.2028"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


def test_get_date_error() -> None:
    with pytest.raises(ValueError):
        get_date("")
