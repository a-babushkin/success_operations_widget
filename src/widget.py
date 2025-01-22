"""
Функция обрабатывает информацию как о картах, так и о счетах
и возвращает строку с замаскированным номером.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_or_account: str) -> str:
    """Обрабатывает информацию как о картах, так и о счетах. Преобразует в маскированный вид"""
    splited_items = type_card_or_account.split()
    if splited_items[0] == "Счет":
        return ' '.join(splited_items[:-1]) + ' ' + get_mask_account(splited_items[-1])
    else:
        return ' '.join(splited_items[:-1]) + ' ' + get_mask_card_number(splited_items[-1])


def get_date(unformated_date: str) -> str:
    """Переформатирует строку с датой"""
    year, month, day = unformated_date[:10].split("-")
    return f"{day}.{month}.{year}"
