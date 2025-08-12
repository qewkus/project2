import json
import os
from typing import Any, Dict, List, Union

import requests
from dotenv import load_dotenv

load_dotenv()


def read_json_file(filename: Union[str, None] = None) -> Union[Any, List]:
    """Функция, которая проверяет наличие файла и читает его."""
    if filename and os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
        if data is None or data == "":
            return []
        else:
            return data
    return []


def currency_conversion(transactions: List[Dict[str, Any]]) -> float:
    """Функция, которая принимает на вход транзакции и возвращает сумму транзакций в рублях."""
    amount = []
    for transaction in transactions:
        trans_code = transaction["operationAmount"]["currency"]["code"]
        if trans_code == "RUB":
            amount.append(float(transaction["operationAmount"]["amount"]))
        else:
            base_url = "https://api.apilayer.com/exchangerates_data/convert"
            url = f"{base_url}?to=RUB&from={trans_code}&amount={transaction['operationAmount']['amount']}"
            token_api = os.getenv("API_KEY")
            payload: Dict[str, Any] = {}
            headers = {"apikey": token_api}

            response = requests.get(url, headers=headers, data=payload)

            results = response.json()
            amount.append(float(results["result"]))

    return round(sum(amount), 2)


# print(currency_conversion(read_json_file("../data/operations.json")))

