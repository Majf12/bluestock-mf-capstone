-- Query 1: Top 5 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- Query 3: SIP Inflow by Year

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_inflow
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Query 5: Funds with Expense Ratio Below 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 6: Top 5 Funds by 5-Year Return

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Query 7: Funds with High Sharpe Ratio

SELECT
    scheme_name,
    sharpe_ratio,
    risk_grade
FROM fact_performance
WHERE sharpe_ratio > 1
ORDER BY sharpe_ratio DESC;

-- Query 8: Average Transaction Amount by Type

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    AVG(amount_inr) AS average_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY average_amount DESC;

-- Query 9: Number of Funds by Risk Grade

SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;

-- Query 10: Funds Outperforming Benchmark

SELECT
    scheme_name,
    return_3yr_pct,
    benchmark_3yr_pct,
    alpha
FROM fact_performance
WHERE return_3yr_pct > benchmark_3yr_pct
ORDER BY alpha DESC
LIMIT 10;