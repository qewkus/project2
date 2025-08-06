import pytest
from typing import List, Dict, Any
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    generator_usd = filter_by_currency(transactions, "USD")
    assert next(generator_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator_usd) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_empty(transactions: List[Dict[str, Any]]) -> None:
    with pytest.raises(StopIteration):
        generator_bel = filter_by_currency(transactions, "BEL")
        assert next(generator_bel)


def test_filter_by_currency_empty_list(transactions: List[Dict[str, Any]]) -> None:
    generator_empty_list = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator_empty_list)


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    generator_descriptions = transaction_descriptions(transactions)
    assert next(generator_descriptions) == "Перевод организации"
    assert next(generator_descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list(transactions: List[Dict[str, Any]]) -> None:
    with pytest.raises(StopIteration):
        generator_empty = transaction_descriptions([])
        assert next(generator_empty)


def test_card_number_generator() -> None:
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002"]
    assert list(card_number_generator(1, 2)) == expected


def test_card_number_generator_range() -> None:
    with pytest.raises(ValueError):
        generator_range = card_number_generator(-1, -5)
        assert next(generator_range)
