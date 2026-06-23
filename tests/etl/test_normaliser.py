from src.etl.normaliser import normalize_year
from src.etl.normaliser import normalize_ticker


def test_normalize_year_2024():
    assert normalize_year("Mar 2024") == "2024"


def test_normalize_year_2018():
    assert normalize_year("Mar 2018") == "2018"


def test_normalize_year_ttm():
    assert normalize_year("TTM") == "TTM"


def test_normalize_ticker_upper():
    assert normalize_ticker("RELIANCE") == "RELIANCE"


def test_normalize_ticker_lower():
    assert normalize_ticker("reliance") == "RELIANCE"


def test_normalize_ticker_spaces():
    assert normalize_ticker("  reliance  ") == "RELIANCE"

def test_normalize_year_2020():
    assert normalize_year("Mar 2020") == "2020"


def test_normalize_year_2021():
    assert normalize_year("Mar 2021") == "2021"


def test_normalize_year_2022():
    assert normalize_year("Mar 2022") == "2022"


def test_normalize_year_2023():
    assert normalize_year("Mar 2023") == "2023"


def test_normalize_ticker_adani():
    assert normalize_ticker("adaniports") == "ADANIPORTS"


def test_normalize_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_infosys():
    assert normalize_ticker("infosys") == "INFOSYS"


def test_normalize_ticker_hdfc():
    assert normalize_ticker("hdfcbank") == "HDFCBANK"