import pytest


@pytest.fixture
def fixture_processing() -> list[dict]:
    """Фикстура для тестирования функций модуля processing. Входные данные"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939767870, "state": "EXECUTED", "date": "2018-06-30T02:09:03.425572"},
        {"id": 615064591, "state": "UNKNOWN", "date": "2016-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_desc_result() -> list[dict]:
    """Фикстура для тестирования функции test_sort_by_date_desc модуля processing.
    Выходные данные отсортированные по убыванию"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939767870, "state": "EXECUTED", "date": "2018-06-30T02:09:03.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "UNKNOWN", "date": "2016-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_asc_result() -> list[dict]:
    """Фикстура для тестирования функции test_sort_by_date_asc модуля processing.
    Выходные данные отсортированные по возрастанию"""
    return [
        {"id": 615064591, "state": "UNKNOWN", "date": "2016-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939767870, "state": "EXECUTED", "date": "2018-06-30T02:09:03.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def fixture_filter_by_state_exec() -> list[dict]:
    """Фикстура для тестирования функции test_filter_by_state_exec модуля processing.
    Выходные данные отфильтрованные по EXECUTED"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939767870, "state": "EXECUTED", "date": "2018-06-30T02:09:03.425572"},
    ]


@pytest.fixture
def fixture_filter_by_state_canc() -> list[dict]:
    """Фикстура для тестирования функции test_filter_by_state_canc модуля processing.
    Выходные данные отфильтрованные по CANCELED"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
