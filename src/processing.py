def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей с данными о банковских операциях,
    возвращает список словарей, у которых ключ state содержит переданное в функцию значение."""
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(list_param: list[dict], order_by: bool = True) -> list[dict]:
    """Функция сортировки списка словарей с данными о банковских операциях,
    возвращает список словарей, отсортированных по дате"""
    return sorted(list_param, key=lambda x: x["date"], reverse=order_by)
