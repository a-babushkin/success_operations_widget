import json
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_transactions_amount, read_json_file


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
    """Тестируем если трансакция не рублевая"""
    mock_convert_currency.return_value = (True, 1)
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}) == 1
    mock_convert_currency.assert_called_once_with(1, "USD", "RUB")


@patch("src.utils.convert_currency")
def test_get_transactions_amount_invalid(mock_convert_currency: Any) -> None:
    """Тестируем если трансакция  с ошибкой"""
    mock_convert_currency.return_value = (False, 0.0)
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "UUU"}}}) == 0.0
    mock_convert_currency.assert_called_once_with(1, "UUU", "RUB")


def test_get_transactions_amount_rub() -> None:
    """Тестируем если трансакция рублевая"""
    assert get_transactions_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1
