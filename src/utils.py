import json
import logging
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
            for item in data:
                item["amount"] = item.get("operationAmount", {}).get("amount")
                item["currency_name"] = item.get("operationAmount", {}).get("currency", {}).get("name")
                item["currency_code"] = item.get("operationAmount", {}).get("currency", {}).get("code")
                if item.get("operationAmount"):
                    del item["operationAmount"]
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
    result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]
    return result


def search_category_in_description(transactions: list[dict], categories: list) -> dict:
    """Подсчитывает количество транзакций в указанных категориях"""
    category_count: dict[str, int] = {}
    for item in categories:
        pattern = re.compile(re.escape(item), re.IGNORECASE)
        result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]
        category_count.update(Counter(x["description"] for x in result))
    return category_count
