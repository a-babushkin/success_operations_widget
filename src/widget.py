"""
Модуль преобразования в маскированный вид и преобразования строки в дату
"""

import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_or_account: str) -> str:
    """Обрабатывает информацию как о картах, так и о счетах. Преобразует в маскированный вид"""
    number = ""
    type_of_symbol = ""
    for symbol in type_card_or_account:
        if symbol.isdigit():
            number += symbol
        if symbol.isalpha():
            type_of_symbol += symbol
        else:
            type_of_symbol += " "
    if type_of_symbol == "" or number == "":
        return "Ошибка! Проверте вводимые данные."
    else:
        type_of_card_account = type_of_symbol.strip()
    if "Счет" in type_of_card_account:
        try:
            number_of_card_account = get_mask_account(number)
        except Exception:
            return "Ошибка! Проверте вводимые данные."
        type_of_card_account = "Счет"
    else:
        try:
            number_of_card_account = get_mask_card_number(number)
        except Exception:
            return "Ошибка! Проверте вводимые данные."
    return type_of_card_account + " " + number_of_card_account


def get_date(unformated_date: str) -> str:
    """Переформатирует строку с датой"""
    date_formats = [
        "%Y-%m-%d",  # 2023-10-25
        "%d/%m/%Y",  # 25/10/2023
        "%m-%d-%Y",  # 10-25-2023
        "%B %d, %Y",  # October 25, 2023
        "%d %B %Y",  # 25 October 2023
        "%Y/%m/%d",  # 2023/10/25
    ]

    for fmt in date_formats:
        try:
            date_object = datetime.strptime(unformated_date, fmt)
            return date_object.strftime("%d.%m.%Y")  # Возвращаем в формате YYYY-MM-DD
        except ValueError:
            continue

    match = re.match(r"(\d{1,2})(?:st|nd|rd|th) (\w{3}) (\d{4})", unformated_date)
    if match:
        day = match.group(1)
        month = match.group(2)
        year = match.group(3)
        month_number = datetime.strptime(month, "%b").month
        formatted_date = f"{day.zfill(2)}.{month_number:02d}.{year}"
        return formatted_date

    return "Неверный формат даты!"
