# Функция
# mask_account_card
# :
# Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки
# в зависимости от типа входных данных (карта или счет).
# Параметризованные тесты с разными типами карт и счетов для проверки
# универсальности функции.
# Тестирование функции на обработку некорректных входных данных и проверка
# ее устойчивости к ошибкам.
from unittest import expectedFailure

# Функция
# get_date
# :
# Тестирование правильности преобразования даты.
# Проверка работы функции на различных входных форматах даты, включая граничные случаи
# и нестандартные строки с датами.
# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.


import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 **** 6361"),
    ("Счет 73654108430135874305", "Счет 4305"),
    ("MasterCard 7000792289606354", "MasterCard 7000 79 **** 6354"),
])

def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


def test_mask_account_card_error():
    with pytest.raises(ValueError):
        mask_account_card("1")


@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2026-08-16T02:26:18.671407", "16.08.2026"),
    ("2028-01-23T02:26:18.671407", "23.01.2028"),
])

def test_get_date(date_string, expected):
    assert get_date(date_string) == expected


def test_get_date_error():
    with pytest.raises(ValueError):
        get_date("")




