def get_mask_card_number(card: str) -> str:
    """Возвращает замаскированный номер карты."""
    return f"{card[:4]} {card[4:6]}** ****{card[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счёта."""
    return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
