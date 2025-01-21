"""
Модуль маскировки вводимых значениц номера карты и счета
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{str(account_number)[-4:]}"


if __name__ == "__main__":
    print("Вы запустили сам модуль! Этого не надо делать.")
