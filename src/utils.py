import json
import logging
import os
import re
from collections import Counter
from typing import Any

from src.external_api import convert_currency

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/" + __name__ + ".log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(path_to_file: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Функция сработала штатно, получены данные: {data}")
            return data
    except FileNotFoundError:
        logger.error(f"Файл по пути {path_to_file} не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Произошла ошибка декодирования JSON в данных")
        return []


def get_transactions_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float."""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if currency_code == "RUB":
        logger.info(f"Трансакция в рублях и равна {amount}")
        return float(amount)
    else:
        logger.info(f"Запрашиваемая трансакция в {currency_code} валюте")
        result = convert_currency(amount, currency_code, "RUB")
        if result[0]:
            logger.info(f"Конвертация прошла успешно. Сумма транзакции = {result[1]}")
            return result[1]
        logger.error("Ошибка конвертации. Возвращаемая сумма транзакции = 0.0")
        return 0.0


def search_substr_in_description(transactions: list[dict], search_str: str) -> list[dict]:
    """Поиск строки в поле описание (description) каждой транзакции из списка транзакций"""
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]
    return result


def search_category_in_description(transactions: list[dict], categories: list) -> dict:
    """Подсчитывает количество транзакций в указанных категориях"""
    category_count = {}
    for item in categories:
        pattern = re.compile(re.escape(item), re.IGNORECASE)
        result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]
        category_count.update(Counter(x['description'] for x in result))
    return category_count


# if __name__ == "__main__":
#     # print(search_category_in_description(
#     #     read_json_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'operations.json')), ['Открытие вклада', 'Перевод организации', 'Перевод с карты']))
#
#     print(search_category_in_description(
#         [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702",
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188",
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160",
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229",
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657",
#             },
#         ], ['1', '2', '3']))
