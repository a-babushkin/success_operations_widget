from typing import Any
from unittest.mock import patch

import pandas as pd

from src.csv_excell import get_transaction_from_csv_file, get_transaction_from_excel_file


@patch("pandas.read_csv")
def test_get_transaction_from_csv_file_ok(mock_read_csv: Any) -> None:
    """Testing the csv file reading function for correct response"""
    mock_data = pd.DataFrame(
        {
            "id": [1, 2],
            "amount": [100.0, 200.0],
            "description": ["Test transaction 1", "Test transaction 2"],
        }
    )
    mock_read_csv.return_value = mock_data
    result = get_transaction_from_csv_file("dummy_path.csv")
    expected_result = [
        {"id": 1, "amount": 100.0, "description": "Test transaction 1"},
        {"id": 2, "amount": 200.0, "description": "Test transaction 2"},
    ]
    assert result == expected_result


@patch("pandas.read_csv")
def test_get_transaction_from_csv_file_not_found(mock_read_csv: Any) -> None:
    """Testing function by raise a FileNotFoundError exception"""
    mock_read_csv.side_effect = FileNotFoundError("File not found")
    result = get_transaction_from_csv_file("non_existent_file.csv")
    assert result == [{}]


@patch("pandas.read_excel")
def test_get_transaction_from_excel_file_ok(mock_read_excel: Any) -> None:
    """Testing the excel file reading function for correct response"""
    mock_data = pd.DataFrame(
        {
            "id": [1, 2],
            "amount": [100.0, 200.0],
            "description": ["Test transaction 1", "Test transaction 2"],
        }
    )
    mock_read_excel.return_value = mock_data
    result = get_transaction_from_excel_file("dummy_path.excel")
    expected_result = [
        {"id": 1, "amount": 100.0, "description": "Test transaction 1"},
        {"id": 2, "amount": 200.0, "description": "Test transaction 2"},
    ]
    assert result == expected_result


@patch("pandas.read_excel")
def test_get_transaction_from_excel_file_not_found(mock_read_excel: Any) -> None:
    """Testing function by raise a FileNotFoundError exception"""
    mock_read_excel.side_effect = FileNotFoundError("File not found")
    result = get_transaction_from_excel_file("non_existent_file.excel")
    assert result == [{}]
