"""
Набор функций, реализующих генераторы для обработки данных
"""

from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции.
    И возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной в currency"""
    if not transactions:
        yield "Пустой список!"
    if not list(filter(lambda x: x["currency_code"] == currency, transactions)):
        yield "Нет такой валюты!"
    for item_trans in filter(lambda x: x["currency_code"] == currency, transactions):
        yield item_trans


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Генератор принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    if not transactions:
        yield "Пустой список!"
    for item_trans in transactions:
        yield item_trans["description"]


def card_number_generator(start: int = 1, finish: int = 9999999999999999) -> Iterator:
    """Генератор выдает номера банковских карт в диапазоне start - finish и в формате XXXX XXXX XXXX XXXX"""
    if start < finish:
        for item_trans in range(start, finish + 1):
            item_card_number = "0" * (16 - len(str(item_trans))) + str(item_trans)
            yield (
                item_card_number[:4]
                + " "
                + item_card_number[4:8]
                + " "
                + item_card_number[8:12]
                + " "
                + item_card_number[12:]
            )
    else:
        yield "Неверный диапазон!"
