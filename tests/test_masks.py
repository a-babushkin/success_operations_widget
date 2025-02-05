import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_str, result",
    [
        ("1596 8378 6870 5199", "1596 83** **** 5199"),
        ("  7158300734726758  ", "7158 30** **** 6758"),
        ("68319824  76737658", "6831 98** **** 7658"),
        ("8990-9221-1366-5229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card_str: str, result: str) -> None:
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card_str) == result


@pytest.mark.parametrize("card_str", ["78687", "715830077868734726758", ""])
def test_get_mask_card_number_not_standard_length(card_str: str) -> None:
    """Тестирование правильности маскирования номера карты при исключениях."""
    with pytest.raises(Exception) as exc_info:
        get_mask_card_number(card_str)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Не стандартный размер номера карты!"


@pytest.mark.parametrize(
    "account_str, result",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_str: str, result: str) -> None:
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(account_str) == result


@pytest.mark.parametrize("account_str", ["78687", "715830077868734726758", ""])
def test_get_mask_account_number_not_standard_length(account_str: str) -> None:
    """Тестирование правильности маскирования номера счета при исключениях."""
    with pytest.raises(Exception) as exc_info:
        get_mask_account(account_str)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Не стандартный размер номера счета!"
