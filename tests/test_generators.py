import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fixture_transactions: list[dict]) -> None:
    """Тестирование фильтрации списка словарей по заданной валюте RUB"""
    generator = filter_by_currency(fixture_transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "amount": "43318.34",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "amount": "67314.70",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }

    generator = filter_by_currency([], "USD")
    assert next(generator) == "Пустой список!"

    generator = filter_by_currency(fixture_transactions, "FR")
    assert next(generator) == "Нет такой валюты!"


def test_transaction_descriptions(fixture_transactions: list[dict]) -> None:
    """Тестирование генератора, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    result = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    generator = transaction_descriptions(fixture_transactions)
    for i in range(3):
        assert next(generator) == result[i]

    generator = transaction_descriptions(fixture_transactions)
    for i in range(5):
        assert next(generator) == result[i]

    generator = transaction_descriptions([])
    assert next(generator) == "Пустой список!"


@pytest.mark.parametrize(
    "start, finish, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (
            2205461285456649,
            2205461285456652,
            ["2205 4612 8545 6649", "2205 4612 8545 6650", "2205 4612 8545 6651", "2205 4612 8545 6652"],
        ),
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, finish: int, result: list[str]) -> None:
    """Тестирование  генератора, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    generator = card_number_generator(start, finish)
    for i in range(finish - start + 1):
        assert next(generator) == result[i]


def test_card_number_generator_wrong_param() -> None:
    """Тестирование  генератора в случае неверного диапазона finish <= start"""

    generator = card_number_generator(135, 76)
    assert next(generator) == "Неверный диапазон!"
