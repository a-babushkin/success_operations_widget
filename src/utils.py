import json
from typing import Any

from src.external_api import convert_currency


def read_json_file(path_to_file: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_transactions_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float."""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if currency_code == "RUB":
        return float(amount)
    else:
        result = convert_currency(amount, currency_code, "RUB")
        if result[0]:
            return result[1]
        return 0.0
