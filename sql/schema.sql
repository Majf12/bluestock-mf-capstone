-- ============================================
-- Bluestock Mutual Fund Analytics Database
-- Database Schema
-- ============================================


-- ============================================
-- 1. Fund Master Dimension Table
-- ============================================

CREATE TABLE IF NOT EXISTS dim_fund (

    amfi_code TEXT PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    risk_grade TEXT

);


-- ============================================
-- 2. NAV Fact Table
-- ============================================

CREATE TABLE IF NOT EXISTS fact_nav (

    amfi_code TEXT,

    nav_date DATE,

    nav REAL,

    daily_return REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);


-- ============================================
-- 3. Transactions Fact Table
-- ============================================

CREATE TABLE IF NOT EXISTS fact_transactions (

    investor_id TEXT,

    transaction_date DATE,

    amfi_code TEXT,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);


-- ============================================
-- 4. Performance Fact Table
-- ============================================

CREATE TABLE IF NOT EXISTS fact_performance (

    amfi_code TEXT,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    plan TEXT,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating REAL,

    risk_grade TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);