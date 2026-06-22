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
