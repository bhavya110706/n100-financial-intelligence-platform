import pandas as pd


def check_primary_key_uniqueness(df, column_name):
    """
    DQ-01
    Check primary key uniqueness.
    """

    duplicates = df[df[column_name].duplicated()]

    return duplicates
def check_company_year_uniqueness(df):
    """
    DQ-02
    Check uniqueness of (company_id, year)
    """

    duplicates = df[
        df.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    return duplicates
def check_foreign_key_integrity(
    child_df,
    parent_df,
    child_column,
    parent_column
):
    """
    DQ-03
    Check foreign key integrity.
    """

    invalid_rows = child_df[
        ~child_df[child_column].isin(
            parent_df[parent_column]
        )
    ]

    return invalid_rows