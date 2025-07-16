from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(operations: List[Dict[str, Any]], state: str, expected: List[Dict[str, Any]]) -> None:
    assert filter_by_state(operations, state) == expected


def test_filter_by_state_empty(operations: List[Dict[str, Any]]) -> None:
    with pytest.raises(KeyError):
        filter_by_state(operations, state="123")


def test_sort_by_date(operations: List[Dict[str, Any]]) -> None:
    sorted_operations_desc = sort_by_date(operations, descending=True)
    sorted_operations_asc = sort_by_date(operations, descending=False)

    # Проверка, что список отсортирован по дате в порядке убывания
    assert sorted_operations_desc == sorted(operations, key=lambda x: x["date"], reverse=True)

    # Проверка, что список отсортирован по дате в порядке возрастания
    assert sorted_operations_asc == sorted(operations, key=lambda x: x["date"])
