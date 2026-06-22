import re


def normalize_year(year):
    """
    Convert year values to integer format.
    Example:
    FY2024 -> 2024
    2024 -> 2024
    """

    if year is None:
        return None

    year = str(year)

    match = re.search(r"(20\d{2})", year)

    if match:
        return int(match.group(1))

    return None


def normalize_ticker(ticker):
    """
    Convert ticker symbols to standard format.
    """

    if ticker is None:
        return None

    return str(ticker).strip().upper()