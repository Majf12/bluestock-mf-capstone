# Bluestock Mutual Fund Analytics
# Data Dictionary

## Project Overview

This document describes the datasets, columns, data types, meanings, and sources used in the Mutual Fund Analytics Capstone project.

---

# 1. Fund Master

**Source:** `data/raw/01_fund_master.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | String | Name of the mutual fund scheme |
| fund_house | String | Mutual fund company or fund house |
| category | String | Broad fund category such as Equity or Debt |
| sub_category | String | Specific category such as Large Cap, Mid Cap, or Liquid |
| plan | String | Mutual fund plan type |
| risk_grade | String | Risk classification of the fund |

---

# 2. NAV History

**Source:** `data/raw/02_nav_history.csv`

**Cleaned File:** `data/processed/clean_nav.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value of the mutual fund |

---

# 3. AUM by Fund House

**Source:** `data/raw/03_aum_by_fund_house.csv`

| Column | Data Type | Description |
|---|---|---|
| fund_house | String | Name of the mutual fund house |
| aum_crore | Float | Assets Under Management in crore |

---

# 4. Monthly SIP Inflows

**Source:** `data/raw/04_monthly_sip_inflows.csv`

| Column | Data Type | Description |
|---|---|---|
| month | Date | Month of the SIP inflow |
| sip_inflow_crore | Float | SIP inflow amount in crore |

---

# 5. Category Inflows

**Source:** `data/raw/05_category_inflows.csv`

| Column | Data Type | Description |
|---|---|---|
| category | String | Mutual fund category |
| month | Date | Month of inflow |
| inflow_crore | Float | Inflow amount in crore |

---

# 6. Industry Folio Count

**Source:** `data/raw/06_industry_folio_count.csv`

| Column | Data Type | Description |
|---|---|---|
| month | Date | Month of measurement |
| folio_count | Integer | Number of investor folios |

---

# 7. Scheme Performance

**Source:** `data/raw/07_scheme_performance.csv`

**Cleaned File:** `data/processed/clean_performance.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | String | Name of the mutual fund |
| fund_house | String | Mutual fund house |
| category | String | Fund category |
| plan | String | Plan type |
| return_1yr_pct | Float | One-year return percentage |
| return_3yr_pct | Float | Three-year return percentage |
| return_5yr_pct | Float | Five-year return percentage |
| benchmark_3yr_pct | Float | Three-year benchmark return |
| alpha | Float | Excess return relative to benchmark |
| beta | Float | Sensitivity to market movements |
| sharpe_ratio | Float | Risk-adjusted return measure |
| sortino_ratio | Float | Downside-risk-adjusted return measure |
| std_dev_ann_pct | Float | Annualised volatility |
| max_drawdown_pct | Float | Maximum observed decline |
| aum_crore | Float | Assets Under Management in crore |
| expense_ratio_pct | Float | Annual fund management expense percentage |
| morningstar_rating | Float | Fund rating |
| risk_grade | String | Risk classification |

---

# 8. Investor Transactions

**Source:** `data/raw/08_investor_transactions.csv`

**Cleaned File:** `data/processed/clean_transactions.csv`

| Column | Data Type | Description |
|---|---|---|
| investor_id | String | Unique investor identifier |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Mutual fund scheme code |
| transaction_type | String | SIP, Lumpsum, or Redemption |
| amount_inr | Float | Transaction amount in INR |
| state | String | Investor state |
| city | String | Investor city |
| city_tier | String | City classification |
| age_group | String | Investor age group |
| gender | String | Investor gender |
| annual_income_lakh | Float | Annual income in lakh |
| payment_mode | String | Mode of payment |
| kyc_status | String | KYC verification status |

---

# 9. Portfolio Holdings

**Source:** `data/raw/09_portfolio_holdings.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| stock_name | String | Name of the stock |
| sector | String | Industry sector |
| weight_pct | Float | Portfolio allocation percentage |

---

# 10. Benchmark Indices

**Source:** `data/raw/10_benchmark_indices.csv`

| Column | Data Type | Description |
|---|---|---|
| index_name | String | Name of benchmark index |
| date | Date | Index date |
| index_value | Float | Value of the benchmark index |

---

# Live NAV Data

**Source:** mfapi.in API

The following schemes were fetched using the MFAPI public API:

| Scheme | AMFI Code |
|---|---|
| HDFC Top 100 | 125497 |
| SBI Bluechip | 119551 |
| ICICI Bluechip | 120503 |
| Nippon Large Cap | 118632 |
| Axis Bluechip | 119092 |
| Kotak Bluechip | 120841 |

---

# Database Tables

The cleaned data is loaded into the SQLite database:

**Database:** `bluestock_mf.db`

| Table | Description |
|---|---|
| dim_fund | Fund master information |
| fact_nav | Historical NAV data |
| fact_transactions | Investor transaction data |
| fact_performance | Scheme performance data |

---

# Data Sources

1. Provided CSV datasets
2. MFAPI public API for live mutual fund NAV data

---

# Data Quality Notes

- NAV data was checked for missing values and invalid NAV values.
- Duplicate NAV records were removed.
- Transaction types were standardised.
- Transaction amounts were validated to be greater than zero.
- KYC status values were checked.
- Performance return columns were converted to numeric values.
- Negative Sharpe ratios were checked.
- Expense ratios were validated against the expected range.
- AMFI scheme codes were validated between fund master and NAV history.