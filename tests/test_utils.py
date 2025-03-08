import json
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_transactions_amount, read_json_file, search_category_in_description, \
    search_substr_in_description


@patch("builtins.open")
@patch("json.load")
def test_read_json_file_success(mock_load: Any, mock_open_file: Any) -> None:
    """Тестируем функцию на успешную работу"""
    mock_open_file.new = mock_open()
    test_value: list[dict] = [{}]
    mock_load.return_value = test_value
    result = read_json_file("")
    assert result == test_value


@patch("builtins.open")
@patch("json.load")
def test_read_json_file_json_decode_error(mock_load: Any, mock_open_file: Any) -> None:
    """Тестируем на неверный формат JSON"""
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("Error", "", 1)
    result = read_json_file("")
    assert result == []


@patch("builtins.open")
def test_read_json_file_not_found(mock_open_file: Any) -> None:
    """Тестируем на отсутствие файла"""
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError
    result = read_json_file("")
    assert result == []


@patch("src.utils.convert_currency")
def test_get_transactions_amount_not_rub(mock_convert_currency: Any) -> None:
    """Тестируем если транзакция не рублевая"""
    mock_convert_currency.return_value = (True, 1)
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}) == 1
    mock_convert_currency.assert_called_once_with(1, "USD", "RUB")


@patch("src.utils.convert_currency")
def test_get_transactions_amount_invalid(mock_convert_currency: Any) -> None:
    """Тестируем если транзакция с ошибкой"""
    mock_convert_currency.return_value = (False, 0.0)
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "UUU"}}}) == 0.0
    mock_convert_currency.assert_called_once_with(1, "UUU", "RUB")


def test_get_transactions_amount_rub() -> None:
    """Тестируем если транзакция рублевая"""
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1


def test_search_substr_in_description_ok(fixture_transactions: list[dict]) -> None:
    """Тестирование поиска строки в описании транзакций, строка найдена"""
    required_result = [{'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                        'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
                        'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
                        'to': 'Visa Platinum 8990922113665229'}]
    assert search_substr_in_description(fixture_transactions, 'Перевод с карты') == required_result


def test_search_substr_in_description_wrong_description(fixture_transactions: list[dict]) -> None:
    """Тестирование поиска строки в описании транзакций, нет искомой транзакции"""
    required_result = []
    assert search_substr_in_description(fixture_transactions, 'Неправильная строка') == required_result


def test_search_category_in_description_ok(fixture_transactions: list[dict]) -> None:
    """Тестирование подсчета кол-ва транзакций в списке категорий, есть хотя бы одна категория"""
    required_result = {'Перевод организации': 2, 'Перевод с карты на карту': 1}
    assert search_category_in_description(fixture_transactions, ['Открытие вклада', 'Перевод организации',
                                                                 'Перевод с карты']) == required_result


def test_search_category_in_description_category_not_found(fixture_transactions: list[dict]) -> None:
    """Тестирование подсчета кол-ва транзакций в списке категорий, нет искомых категорий"""
    required_result = {}
    assert search_category_in_description(fixture_transactions, ['1', '2', '3']) == required_result
