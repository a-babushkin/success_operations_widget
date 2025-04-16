from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_exec(fixture_processing: list[dict], fixture_filter_by_state_exec: str) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу EXECUTED"""
    assert filter_by_state(fixture_processing, "EXECUTED") == fixture_filter_by_state_exec


def test_filter_by_state_canc(fixture_processing: list[dict], fixture_filter_by_state_canc: str) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу CANCELED"""
    assert filter_by_state(fixture_processing, "CANCELED") == fixture_filter_by_state_canc


def test_sort_by_date_desc(fixture_processing: list[dict], sort_by_date_desc_result: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания."""
    assert sort_by_date(fixture_processing) == sort_by_date_desc_result
    assert sort_by_date(fixture_processing, True) == sort_by_date_desc_result


def test_sort_by_date_asc(fixture_processing: list[dict], sort_by_date_asc_result: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам в порядке возрастания."""
    assert sort_by_date(fixture_processing, False) == sort_by_date_asc_result
