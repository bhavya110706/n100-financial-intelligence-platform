import pandas as pd

from validator import  (
    check_primary_key_uniqueness,
    check_company_year_uniqueness,
    check_foreign_key_integrity,
    check_balance_sheet_balance,
    check_opm_crosscheck,
    check_positive_sales
)

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

profitandloss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

balancesheet = pd.read_excel(
    "data/raw/balancesheet.xlsx",
    header=1
)

results = []

# DQ-01
results.append({
    "rule_id": "DQ-01",
    "severity": "CRITICAL",
    "table_name": "companies",
    "issue_count": len(
        check_primary_key_uniqueness(
            companies,
            "id"
        )
    ),
    "description": "Primary key duplicates"
})

# DQ-02
results.append({
    "rule_id": "DQ-02",
    "severity": "CRITICAL",
    "table_name": "profitandloss",
    "issue_count": len(
        check_company_year_uniqueness(
            profitandloss
        )
    ),
    "description": "Duplicate company/year combinations"
})

# DQ-03
results.append({
    "rule_id": "DQ-03",
    "severity": "CRITICAL",
    "table_name": "profitandloss",
    "issue_count": len(
        check_foreign_key_integrity(
            profitandloss,
            companies,
            "company_id",
            "id"
        )
    ),
    "description": "Foreign key violations"
})

# DQ-04
results.append({
    "rule_id": "DQ-04",
    "severity": "WARNING",
    "table_name": "balancesheet",
    "issue_count": len(
        check_balance_sheet_balance(
            balancesheet
        )
    ),
    "description": "Assets vs liabilities mismatch"
})

# DQ-05
results.append({
    "rule_id": "DQ-05",
    "severity": "WARNING",
    "table_name": "profitandloss",
    "issue_count": len(
        check_opm_crosscheck(
            profitandloss
        )
    ),
    "description": "OPM mismatch"
})

# DQ-06
results.append({
    "rule_id": "DQ-06",
    "severity": "WARNING",
    "table_name": "profitandloss",
    "issue_count": len(
        check_positive_sales(
            profitandloss
        )
    ),
    "description": "Non-positive sales"
})

report = pd.DataFrame(results)

report.to_csv(
    "output/validation_failures.csv",
    index=False
)

print(report)
print("\nvalidation_failures.csv generated successfully")