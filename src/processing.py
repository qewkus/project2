operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Возвращает новый список словарей, у которых ключ соответствует значению."""
    filter = []
    for operation in operations:
        if operation.get("state") == state:
            filter.append(operation)
    return filter


print(filter_by_state(operations, state="CANCELED"))


def sort_by_date(operations: list, descending: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате."""
    return sorted(operations, key=lambda operation: operation["date"], reverse=descending)


print(sort_by_date(operations, descending=False))
