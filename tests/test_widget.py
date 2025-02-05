import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card_str, result",
    [
        ("Maestro 1596-8378-6870-5199", "Maestro 1596 83** **** 5199"),
        ("Счет 6468 6473 6788 9477 9589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        (" %Счет% 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa+Platinum 8990_9221_1366_5229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет в банке 73654108430135874305", "Счет **4305"),
        ("78687", "Ошибка! Проверте вводимые данные."),
        ("715830077868734726758", "Ошибка! Проверте вводимые данные."),
        ("", "Ошибка! Проверте вводимые данные."),
        ("Only letters", "Ошибка! Проверте вводимые данные."),
        ("Счет 4636", "Ошибка! Проверте вводимые данные."),
    ],
)
def test_mask_account_card(account_card_str: str, result: str) -> None:
    assert mask_account_card(account_card_str) == result


@pytest.mark.parametrize(
    "date_str, result",
    [
        ("2023-10-25", "25.10.2023"),
        ("25/10/2023", "25.10.2023"),
        ("10-25-2023", "25.10.2023"),
        ("October 25, 2023", "25.10.2023"),
        ("25 October 2023", "25.10.2023"),
        ("2023/10/25", "25.10.2023"),
        ("25th Oct 2023", "25.10.2023"),
        ("Invalid Date", "Неверный формат даты!"),
        ("", "Неверный формат даты!"),
    ],
)
def test_get_date(date_str: str, result: str) -> None:
    assert get_date(date_str) == result
