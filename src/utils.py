import json
import os
import requests
import logging
from typing import Any, Dict, List, Union
from dotenv import load_dotenv
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT_DIR / 'logs'

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_DIR/'utils.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    encoding='utf-8'
)

logger = logging.getLogger('utils')

load_dotenv()


def read_json_file(filename: Union[str, None] = None) -> Union[Any, List]:
    """Функция, которая проверяет наличие файла и читает его."""
    if filename and os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
        if data is None or data == "":
            logger.warning("Пустой файл")
            return []
        else:
            logger.info("Всё хорошо")
            return data
    return []


def currency_conversion(transactions: List[Dict[str, Any]]) -> float:
    """Функция, которая принимает на вход транзакции и возвращает сумму транзакций в рублях."""
    total_amount_rub = 0.0
    for transaction in transactions:
        operation_amount = transaction["operationAmount"]
        amount = float(operation_amount["amount"])
        code = operation_amount["currency"]["code"]
        if code == "RUB":
            logger.debug("Конвертация не требуется")
            total_amount_rub += amount
        else:
            base_url = "https://api.apilayer.com/exchangerates_data/convert"
            url = f"{base_url}?to=RUB&from={code}&amount={transaction['operationAmount']['amount']}"
            token_api = os.getenv("API_KEY")
            payload: Dict[str, Any] = {}
            headers = {"apikey": token_api}

            response = requests.get(url, headers=headers, data=payload)

            results = response.json()
            converted_amount = float(results['operationAmount']['amount'])
            total_amount_rub += converted_amount
    logger.info("Всё окей")
    return round(total_amount_rub)


print(currency_conversion(read_json_file("../data/operations.json")))
