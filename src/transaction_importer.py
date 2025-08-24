import os
from typing import Dict, List

import pandas as pd

# Определяем путь к файлам
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_1 = os.path.join(ROOT_DIR, "..", "data", "transactions.csv")
FILE_PATH_2 = os.path.join(ROOT_DIR, "..", "data", "transactions_excel.xlsx")


def reading_operations_from_csv(file_path: str, encoding: str = "utf-8") -> List[Dict]:
    """Преобразуем файл из формата CSV в словарь"""
    dataframe = pd.read_csv(file_path, encoding=encoding, sep=';')
    return dataframe.to_dict("records")


# print(reading_operations_from_csv(FILE_PATH_1))


def reading_operations_from_excel(file_path: str) -> List[Dict]:
    """Преобразуем файл из формата EXCEL в словарь"""
    dataframe = pd.read_excel(file_path, engine="openpyxl")
    return dataframe.to_dict("records")


# print(reading_operations_from_excel(FILE_PATH_2))
