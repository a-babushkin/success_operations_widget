"""
Модуль декораторов
"""

import time
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Внешняя функция, декоратор с параметрами"""

    def write_log(message: str) -> None:
        """Функция вывода логирования либо в файл, либо в консоль"""
        if filename:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(message + "\n")
        else:
            print(message)

    def log_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Декоратор логирования"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция обертка."""
            start = time.time()
            write_log(f'Function "{func.__name__}" start with args: {args} {kwargs}')
            try:
                result = func(*args, **kwargs)
                finish = time.time()
                write_log(
                    f"{func.__name__} ok! \n"
                    f'Function "{func.__name__}" successfully finished, result = {result} \n'
                    f"Time wasted: {finish - start:.6f}"
                )
                return result
            except Exception as e:
                write_log(f"{func.__name__} error: {e}. Inputs: {args} {kwargs}")
                raise

        return wrapper

    return log_decorator
