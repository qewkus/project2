import re
from typing import List, Dict
from collections import Counter


def process_bank_search(data: list[dict], search_str: str) -> list[dict]:
    """ Возвращает список транзакций, описания которых содержат заданную строку """
    if not data:
        raise ValueError("Список словарей пуст")
    else:
        filtered_data = []
        pattern = re.compile(search_str, re.IGNORECASE)

        for dict_ in data:
            description = dict_.get('description', '')
            if isinstance(description, str) and pattern.search(description):
                filtered_data.append(dict_)

        return filtered_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """ Возвращает словарь с количеством операций в каждой категории """
    if not data:
        raise ValueError("Список словарей пуст")
    elif not categories:
        raise ValueError("Список категорий пуст")
    else:
        result = []

        for dict_ in data:
            description = dict_.get('description', '')
            if description in categories:
                result.append(description)

    counted = Counter(result)

    return counted