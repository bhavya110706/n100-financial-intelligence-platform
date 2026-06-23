# Data Quality Findings

## DQ-02: Duplicate Company-Year Records

Severity: CRITICAL

Table: profitandloss

Issue Count: 26

Affected Company:

* ADANIPORTS

Description:
Duplicate records were found for the same combination of company_id and year.

---

## DQ-03: Foreign Key Integrity Failure

Severity: CRITICAL

Table: profitandloss

Issue Count: 99

Description:
Some company_id values exist in profitandloss.xlsx but are missing from companies.xlsx.

Affected Companies:

* ULTRACEMCO
* UNIONBANK
* UNITDSPR
* VBL
* VEDL
* WIPRO
* ZYDUSLIFE
* ZOMATO

Root Cause:
companies.xlsx contains 92 companies while profitandloss.xlsx contains records for 100 companies.

Status:
Requires business review before production loading.

# DQ Investigation Notes

## DQ-05 OPM Cross Check

Validation rule:

OPM = (Operating Profit / Sales) × 100

Result:

234 records flagged.

Example:

AXISBANK Mar 2013

Stored OPM = 1353

Calculated OPM ≈ 30.58

Several banking companies contain unrealistic OPM values including large positive and negative percentages.

Decision:

Flagged as data quality issues and retained in validation report for review.


## DQ-06 Positive Sales Check

Validation rule:

Sales must be greater than zero.

Result:

1 record flagged.

Record:

ADANIENSOL | Mar 2014 | Sales = 0

Decision:

Flagged as a data quality issue and included in validation report.
