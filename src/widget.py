from datetime import datetime


def mask_account_card(info: str) -> str:
    """Функция предназначена для маскировки номера и счёта банковской карты."""
    parts = info.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if card_type.lower().startswith(("visa", "mastercard", "maestro")):
        # Маскировка для карт
        return f"{card_type} {number[:4]} {number[4:6]} **** {number[-4:]}"

    elif card_type.lower() == "счет":
        # Маскировка для счёта
        return f"{card_type} {number[-4:]}"
    else:
        raise ValueError("Неизвестный тип карты или счёта")


# Примеры использования
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """Возвращаю строку с датой."""
    # Разбираю строку даты и времени в объект datetime
    if date_string == "":
        raise ValueError("Вы не ввели дату")
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматирую объект datetime в строку формата "ДД.ММ.ГГГГ"
    return f"{date_obj.day:02}.{date_obj.month:02}.{date_obj.year}"


# Примеры использования
print(get_date("2024-03-11T02:26:18.671407"))
