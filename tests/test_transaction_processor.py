from collections import Counter

from src.transaction_processor import process_bank_operations, process_bank_search


def test_case_insensitivity() -> None:
    """Тест на регистронезависимость"""
    data = [
        {"description": "Оплата за интернет"},
        {"description": "перевод средств"},
        {"description": "Покупка в магазине"},
        {"description": "ОПЛАТА ЗА МОБИЛЬНУЮ СВЯЗЬ"},
        {"description": "Покупка в магазине"},
    ]

    result_lower = process_bank_search(data, "оплата")
    result_upper = process_bank_search(data, "ОПЛАТА")
    result_mixed = process_bank_search(data, "ОпЛата")

    assert result_lower == result_upper
    assert result_lower == result_mixed

    assert len(result_lower) == 2


def test_search_not_found() -> None:
    """Тест на отсутствие результатов поиска"""
    data = [
        {"description": "Оплата за интернет"},
        {"description": "перевод средств"},
        {"description": "Покупка в магазине"},
    ]

    result = process_bank_search(data, "неизвестный запрос")
    assert result == []


def test_empty_data() -> None:
    """Тест на пустой список данных"""
    try:
        process_bank_search([], "оплата")
    except ValueError as e:
        assert str(e) == "Список словарей пуст"


def test_process_bank_operations() -> None:
    """Тестирование функции process_bank_operations"""

    # Подготовка данных
    data = [
        {"description": "Оплата за интернет"},
        {"description": "Перевод средств"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата за интернет"},
        {"description": "Оплата за мобильную связь"},
        {"description": "Покупка в магазине"},
    ]

    categories = ["Оплата за интернет", "Покупка в магазине", "Перевод средств"]

    result = process_bank_operations(data, categories)
    expected_result = Counter({"Оплата за интернет": 2, "Перевод средств": 1, "Покупка в магазине": 2})

    assert result == expected_result, f"Ожидалось: {expected_result}, Получено: {result}"

    try:
        process_bank_operations([], categories)
    except ValueError as e:
        assert str(e) == "Список словарей пуст"


if __name__ == "__main__":
    test_case_insensitivity()
    test_search_not_found()
    test_empty_data()
    test_process_bank_operations()
