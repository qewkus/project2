import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction_importer import reading_operations_from_csv, reading_operations_from_excel
from src.transaction_processor import process_bank_search
from src.utils import filter_by_currency_csv_and_excel, read_json_file

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_1 = os.path.join(ROOT_DIR, "data", "operations.json")
FILE_PATH_2 = os.path.join(ROOT_DIR, "data", "transactions.csv")
FILE_PATH_3 = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print("Выберите необходимый пункт меню:\n")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла\n")

    user_input = int(input("Ваш выбор: "))
    if user_input == 1:
        choosen_data = read_json_file(FILE_PATH_1)
        print("Для обработки выбран JSON-файл.")
    elif user_input == 2:
        choosen_data = reading_operations_from_csv(FILE_PATH_2)
        print("Для обработки выбран CSV-файл.")
    elif user_input == 3:
        choosen_data = reading_operations_from_excel(FILE_PATH_3)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Не корректный ввод.")
        return

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING).\n")
        status_input = input("Статус: ").upper()
        if status_input in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            filtered_transactions = filter_by_state(choosen_data, status_input)
            print(filtered_transactions)
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    while True:
        filtered_transactions = choosen_data
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == "да":
            choosen_data = sort_by_date(filtered_transactions, descending=True)
            print(choosen_data)
            break
        elif sort_choice == "нет":
            choosen_data = filtered_transactions
            print(choosen_data)
            break
        else:
            print("Неккоректный ввод")

    while True:
        order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if order_choice == "по возрастанию":
            choosen_order = choosen_data
            print(choosen_order)
            break
        elif order_choice == "по убыванию":
            choosen_order = sort_by_date(choosen_data, descending=False)
            print(choosen_order)
            break
        else:
            print("Неккоректный ввод")

    while True:
        currency_filter = input("Выводить только рублёвые транзакции? Да/Нет: ").strip().lower()
        if currency_filter == "да":
            if user_input == 1:
                choosen_currency = list(filter_by_currency(choosen_order, "RUB"))
                print(choosen_currency)
                break
            elif user_input == 2 or user_input == 3:
                choosen_currency = list(filter_by_currency_csv_and_excel(choosen_order, "RUB"))
                print(choosen_currency)
                break
        elif currency_filter == "нет":
            choosen_currency = choosen_order
            print(choosen_currency)
            break
        else:
            print("Неккоректный ввод")

    while True:
        description_filter = (
            input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет: ").strip().lower()
        )
        if description_filter == "да":
            search_str = str(input("Введите фразу: Перевод с карты на карту, Перевод организации, Открытие вклада: "))
            choosen_description = process_bank_search(choosen_currency, search_str)
            print(choosen_description)
            break
        elif description_filter == "нет":
            choosen_description = choosen_currency
            print(choosen_description)
            break
        else:
            print("Неккоректный ввод")

    print("Распечатываю итоговый список транзакций...")

    choosen_description = list(choosen_description)
    if not choosen_description:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(choosen_description)}")
        for transaction in choosen_description:
            print(transaction)


if __name__ == "__main__":
    main()
