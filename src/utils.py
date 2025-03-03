import json
import logging
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
