import os
from typing import Any

from src.csv_excell import get_transaction_from_csv_file, get_transaction_from_excel_file
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file, search_substr_in_description
from src.widget import get_date, mask_account_card


def data_processing(data_from_file: list[dict]) -> None:
    state = choose_state()
    filter_state = filter_by_state(data_from_file, state)
    options = additional_questions()
    if options["sort_by_date"]:
        data_sorted = sort_by_date(filter_state, options["sort_revers"])
    else:
        data_sorted = filter_state
    if options["rub_transactions"]:
        filter_currency = []
        for transaction in filter_by_currency(data_sorted, "RUB"):
            filter_currency.append(transaction)
    else:
        filter_currency = data_sorted
    if options["filter_by_word"]:
        final_data = search_substr_in_description(filter_currency, options["filter_by_word"])
    else:
        final_data = filter_currency
    if len(final_data):
        print(f"Всего банковских операций в выборке: {len(final_data)}", end="\n\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    for item in final_data:
        print(f"{get_date(str(item.get('date')))} {item.get('description')}")
        if item.get("from") and type(item.get("from")) != float:
            print(f"{mask_account_card(str(item.get('from')))} -> ", end="")
        print(mask_account_card(str(item.get("to"))))
        print(f"Сумма: {item.get('amount')} {item.get('currency_code')}", end="\n\n")


def run_start_menu() -> None:
    """Запускает начальное меню для выбора типа файла данных"""
    while True:
        user_input = input(
            """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
        )
        try:
            selected_menu = int(user_input)
            file_name = os.path.dirname(__file__)
            match selected_menu:
                case 1:
                    print("Для обработки выбран JSON-файл.")
                    data_processing(read_json_file(os.path.join(file_name, "data", "operations.json")))
                    return
                case 2:
                    print("Для обработки выбран CSV-файл.")
                    data_processing(get_transaction_from_csv_file(os.path.join(file_name, "data", "transactions.csv")))
                    return
                case 3:
                    print("Для обработки выбран XLSX-файл.")
                    data_processing(
                        get_transaction_from_excel_file(os.path.join(file_name, "data", "transactions_excel.xlsx"))
                    )
                    return
                case _:
                    print("Неверный выбор! Попробуйте еще раз.")
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, попробуйте снова.")


def choose_state() -> str:
    """Осуществляет выбор статуса операции"""
    while True:
        user_input = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """
        )
        try:
            selected_status = user_input.upper()
            if selected_status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу {selected_status}.")
                return selected_status
            else:
                print(f"Статус операции {selected_status} недоступен.")
        except ValueError:
            print("Ошибка: Пожалуйста, попробуйте снова.")


def additional_questions() -> Any:
    answers: Any = {}
    while True:
        input_value = input("Отсортировать операции по дате? Да / Нет").lower()
        if input_value in ["да", "д"]:
            answers["sort_by_date"] = True
            while True:
                input_value = input("Отсортировать по возрастанию или по убыванию?").lower()
                if input_value in ["по возрастанию", "в"]:
                    answers["sort_revers"] = False
                    break
                elif input_value in ["по убыванию", "у"]:
                    answers["sort_revers"] = True
                    break
                else:
                    print("Можно выбрать только по возрастанию или по убыванию")
            break
        elif input_value in ["нет", "н"]:
            answers["sort_by_date"] = False
            break
        else:
            print("Можно выбрать только Да или Нет")

    while True:
        input_value = input("Выводить  только  рублевые транзакции? Да / Нет").lower()
        if input_value in ["да", "д"]:
            answers["rub_transactions"] = True
            break
        elif input_value in ["нет", "н"]:
            answers["rub_transactions"] = False
            break
        else:
            print("Можно выбрать только Да или Нет")

    while True:
        input_value = input("Отфильтровать список транзакций по определенному слову в описании? Да / Нет").lower()
        if input_value in ["да", "д"]:
            answers["filter_by_word"] = input("Введите слово")
            break
        elif input_value in ["нет", "н"]:
            answers["filter_by_word"] = ""
            break
        else:
            print("Можно выбрать только Да или Нет")
    return answers


if __name__ == "__main__":
    run_start_menu()
