from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_exec(fixture_processing: list[dict], fixture_filter_by_state_exec: str) -> None:
    assert filter_by_state(fixture_processing, "EXECUTED") == fixture_filter_by_state_exec


def test_filter_by_state_canc(fixture_processing: list[dict], fixture_filter_by_state_canc: str) -> None:
    assert filter_by_state(fixture_processing, "CANCELED") == fixture_filter_by_state_canc


def test_sort_by_date_desc(fixture_processing: list[dict], sort_by_date_desc_result: list[dict]) -> None:
    assert sort_by_date(fixture_processing) == sort_by_date_desc_result
    assert sort_by_date(fixture_processing, True) == sort_by_date_desc_result


def test_sort_by_date_asc(fixture_processing: list[dict], sort_by_date_asc_result: list[dict]) -> None:
    assert sort_by_date(fixture_processing, False) == sort_by_date_asc_result
