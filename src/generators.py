"""Набор функций, реализующих генераторы для обработки данных"""

from collections.abc import Iterator


def filter_by_currency(transaction_list: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    И возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной в currency"""
    filtered_transactions = list(
        filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transaction_list)
    )
    for item_trans in filtered_transactions:
        yield item_trans


def transaction_descriptions(transaction_list: list[dict]) -> Iterator[dict]:
    """Генератор принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    filtered_description = list(map(lambda x: x["description"], transaction_list))
    for item_trans in filtered_description:
        yield item_trans


def card_number_generator(start: int = 1, finish: int = 9999999999999999) -> Iterator[str]:
    """Генератор выдает номера банковских карт в диапазоне start - finish и в формате XXXX XXXX XXXX XXXX"""
    if start < finish:
        for item_trans in range(start, finish + 1):
            item_card_number = "0" * (16 - len(str(item_trans))) + str(item_trans)
            yield item_card_number[:4] + " " + item_card_number[4:9] + " " + item_card_number[
                                                                             8:13
                                                                             ] + " " + item_card_number[12:]
    else:
        yield "Неверный диапазон!"
