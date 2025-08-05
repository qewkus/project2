def get_mask_card_number(card: str) -> str:
    """Возвращает замаскированный номер карты."""
    if len(card) > 16:
        raise ValueError("Номер счёта слишком длинный")
    elif len(card) == 0:
        raise ValueError("Вы ввели пустую строку или номер карты")
    elif len(card) < 16:
        raise ValueError("Номер счёта слишком короткий")
    else:
        return f"{card[:4]} {card[4:6]}** ****{card[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счёта."""
    if len(account_number) > 20:
        raise ValueError("Номер счёта слишком длинный")
    elif len(account_number) < 20:
        raise ValueError("Номер счёта слишком короткий")
    else:
        return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
