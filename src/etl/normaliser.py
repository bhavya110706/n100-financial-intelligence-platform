def normalize_year(year):
    """
    Convert values like:
    Mar 2024 -> 2024
    Mar 2019 -> 2019
    TTM -> TTM
    """

    if str(year).strip().upper() == "TTM":
        return "TTM"

    return str(year).split()[-1]


def normalize_ticker(ticker):
    """
    Standardize ticker names.

    Example:
    adaniports -> ADANIPORTS
    Reliance -> RELIANCE
    """

    return str(ticker).strip().upper()