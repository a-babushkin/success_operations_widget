# Проект Виджет для личного кабинета клиента банка.

## Описание:

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/a-babushkin/success_operations_widget.git
```
2. Установите зависимости:
```
poetry install
```
## Зависимости:

```requires-python = ">=3.11"
dependencies = [
    "python-dotenv (>=1.0.1,<2.0.0)",
    "requests (>=2.32.3,<3.0.0)",
    "pandas (>=2.2.3,<3.0.0)",
    "openpyxl (>=3.1.5,<4.0.0)",
    "pandas-stubs (>=2.2.3.241126,<3.0.0.0)"
]

[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.1"
mypy = "^1.14.1"
black = "^24.10.0"
isort = "^5.13.2"


[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Настройки Линтеров

```
[tool.black]
line-length = 119
exclude = ".git"

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = 'venv'
```

## Использование:

1. Авторизуйтесь на сайте банка.
2. Зайдите в личный кабинет.
3. Выберите из списка этот виджет и запустите его.
4. Запустить можно и в исполняемой среде Python
5. Запускать нужно файл `main.py`

## Тестирование:

- В проекте установлен Pytest фрэймворк и pytest-cov библиотека;
- Прописаны тесты для всех модулей;
- Покрытие тестами проекта равно 100%;
- В папке htmlcov лежит отчет покрытия тестами;
- Добавлено тестирование модуля generators;
- Обновлен отчет покрытия в папке htmlcov;
- Добавлено тестирование модуля decorators;
- Еще раз обновлен отчет покрытия в папке htmlcov;
- Добавлено тестирование на все новые функции;

Для самостоятельной проверки покрытия тестами проекта 
запустите в Терминале команду `pytest --cov`
Ддя получения отчета о тестовом покрытии 
запустите в Терминале команду `pytest --cov=src --cov-report=html`

## Добавление новых функций:

- Модуль Генераторов (filter_by_currency(), transaction_descriptions(), card_number_generator())
- Чтение JSON файла (read_json_file())
- Выделение суммы из трансакции (get_transactions_amount())
- Конвертация валюты спомощью внешнего API (convert_currency())
- Чтение CSV а файла (get_transaction_from_csv_file())
- Чтение Excell файла (get_transaction_from_excel_file())
- Поиск подстроки в описании (search_substr_in_description)
- Подсчет категорий и их кол-во (search_category_in_description)

## Документация:

Для получения дополнительной информации обратитесь в службу поддержки по телефонам указанным в контактах.

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://opensource.org/license/mit).