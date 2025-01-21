"""
Модуль маскировки вводимых значениц номера карты и счета
"""


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_string = str(card_number)

    return f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account_number = f"**{str(account_number)[-4:]}"

    return mask_account_number


if __name__ == "__main__":
    print('Вы запустили сам модуль! Этого не надо делать.')
