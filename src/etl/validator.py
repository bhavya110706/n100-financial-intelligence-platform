import pandas as pd


def check_primary_key_uniqueness(df, column_name):
    """
    DQ-01
    Check primary key uniqueness.
    """

    duplicates = df[df[column_name].duplicated()]

    return duplicates