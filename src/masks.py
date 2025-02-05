"""
Модуль маскировки вводимых значениц номера карты и счета
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    number = ""
    for symbol in card_number:
        if symbol.isdigit():
            number += symbol
    if len(number) != 16:
        raise Exception("Не стандартный размер номера карты!")
    else:
        return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    number = ""
    for symbol in account_number:
        if symbol.isdigit():
            number += symbol
    if len(number) != 20:
        raise Exception("Не стандартный размер номера счета!")
    else:
        return f"**{str(number)[-4:]}"
