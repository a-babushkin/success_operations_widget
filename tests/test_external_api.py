from typing import Any
from unittest.mock import patch

from src.external_api import convert_currency


@patch("requests.get")
def test_convert_currency_ok(mock_get: Any) -> None:
    """Тестирование функции конвертирования валюты корректный ответ"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1}
    assert convert_currency(100, "USD", "RUB") == (True, 1)


@patch("requests.get")
def test_convert_currency_error(mock_get: Any) -> None:
    """Тестирование функции конвертирования валюты на ошибку"""
    mock_get.return_value.json.return_value = {"message": "Error"}
    assert convert_currency(100, "DSU", "RUB") == (False, 0.0)
