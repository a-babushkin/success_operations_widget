def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей с данными о банковских операциях,
    возвращает список словарей, у которых ключ state содержит переданное в функцию значение."""
    return [transaction for transaction in transactions if transaction['state'] == state]