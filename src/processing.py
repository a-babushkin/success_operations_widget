"""
Модуль фильтрации и сортировки вводимого списка словарей карты и счета
"""


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей с данными о банковских операциях,
    возвращает список словарей, у которых ключ state содержит переданное в функцию значение."""
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse_direction: bool = True) -> list[dict]:
    """Функция сортировки списка словарей с данными о банковских операциях,
    возвращает список словарей, отсортированных по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse_direction)
