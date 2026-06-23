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
    Check uniqueness of (company_id, year).
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


def check_balance_sheet_balance(bs_df):
    """
    DQ-04
    Total Assets should approximately equal Total Liabilities.
    Difference must be less than 1%.
    """
    diff_percent = (
        abs(
            bs_df["total_assets"]
            - bs_df["total_liabilities"]
        )
        / bs_df["total_assets"]
    ) * 100

    failures = bs_df[diff_percent > 1]

    return failures


def check_opm_crosscheck(pl_df):
    """
    DQ-05
    Verify OPM percentage using:

    (Operating Profit / Sales) * 100
    """
    calculated_opm = (
        pl_df["operating_profit"]
        / pl_df["sales"]
    ) * 100

    diff = abs(
        calculated_opm
        - pl_df["opm_percentage"]
    )

    failures = pl_df[
        (diff > 5)
        & (pl_df["sales"] > 0)
    ]

    return failures


def check_positive_sales(pl_df):
    """
    DQ-06
    Sales should be positive.
    """
    failures = pl_df[
        pl_df["sales"] <= 0
    ]

    return failures