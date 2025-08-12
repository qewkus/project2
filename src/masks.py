import logging
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT_DIR / "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_DIR / "masks.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)

logger = logging.getLogger("masks")


def get_mask_card_number(card: str) -> str:
    """Возвращает замаскированный номер карты."""
    if len(card) > 16:
        logger.error("Номер счёта слишком длинный")
        raise ValueError("Номер счёта слишком длинный")
    elif len(card) == 0:
        logger.error("ы ввели пустую строку или номер карты")
        raise ValueError("Вы ввели пустую строку или номер карты")
    elif len(card) < 16:
        logger.error("Ночер счёта слишком короткий")
        raise ValueError("Номер счёта слишком короткий")
    else:
        logger.info("Номер карты успешно замаскирован")
        return f"{card[:4]} {card[4:6]}** ****{card[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счёта."""
    if len(account_number) > 20:
        logger.error("Номер счёта слишком длинный")
        raise ValueError("Номер счёта слишком длинный")
    elif len(account_number) < 20:
        logger.error("Номер счёта слишком короткий")
        raise ValueError("Номер счёта слишком короткий")
    else:
        logger.info("Номер счёта успешно замаскирован")
        return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))


if __name__ == "__main__":
    try:
        masked_card = get_mask_card_number("567812345678")
        print(masked_card)
    except ValueError as ex:
        print(f"Ошибка: {ex}")

    try:
        masked_account = get_mask_account("123456789012345678906789")
        print(masked_account)
    except ValueError as ex:
        print(f"Ошибка: {ex}")
