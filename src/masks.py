"""
Модуль маскировки вводимых значениц номера карты и счета
"""

import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/" + __name__ + ".log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    number = ""
    for symbol in card_number:
        if symbol.isdigit():
            number += symbol
    if len(number) != 16:
        logger.error("Не стандартный размер номера карты!")
        raise Exception("Не стандартный размер номера карты!")
    else:
        card_mask = f"{number[:4]} {number[4:6]}** **** {number[12:]}"
        logger.info(f"Возвращает маскированный номер карточки: {card_mask}")
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    number = ""
    for symbol in account_number:
        if symbol.isdigit():
            number += symbol
    if len(number) != 20:
        logger.error("Не стандартный размер номера счета!")
        raise Exception("Не стандартный размер номера счета!")
    else:
        account_mask = f"**{str(number)[-4:]}"
        logger.info(f"Возвращает маскированный номер счета: {account_mask}")
        return account_mask
