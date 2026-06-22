from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)


def test_normalize_year():
    assert normalize_year("FY2024") == 2024
    assert normalize_year("2023") == 2023
    assert normalize_year(2022) == 2022


def test_normalize_ticker():
    assert normalize_ticker("tcs") == "TCS"
    assert normalize_ticker(" infy ") == "INFY"
    assert normalize_ticker("RELIANCE") == "RELIANCE"