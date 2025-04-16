import os
import tempfile
from typing import Any

import pytest

from src.decorators import log


@log()
def divide(a: int, b: int) -> float:
    """Проверочная функция для декоратора @log, деления одного числа на другое"""
    return a / b


def test_log_console_output(capsys: Any) -> None:
    """Тестирование декоратора @log при успешном выводе в консоль"""
    divide(10, 2)
    captured = capsys.readouterr()
    assert "divide ok!" in captured.out


def test_log_console_error(capsys: Any) -> None:
    """Тестирование декоратора @log при ошибочном выводе в консоль"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "divide error" in captured.out


def test_log_file_output() -> None:
    """Тестирование декоратора @log при успешном выводе в файл логирования"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name

    @log(filename=temp_filename)
    def add(a: int, b: int) -> int:
        """Проверочная функция для декоратора @log, сложения одного числа с другим"""
        return a + b

    add(5, 3)
    with open(temp_filename, "r") as f:
        log_content = f.read()

    assert "add ok!" in log_content

    os.remove(temp_filename)


def test_log_file_error() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name

    @log(filename=temp_filename)
    def add(a: int, b: int) -> int:
        """Проверочная функция для декоратора @log, сложения одного числа с другим"""
        return a + b

    with pytest.raises(TypeError):
        add(5, "3")

    with open(temp_filename, "r") as f:
        log_content = f.read()

    assert "add error:" in log_content

    os.remove(temp_filename)
