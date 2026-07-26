import sqlite3


# Connect to database
connection = sqlite3.connect(
    "bluestock_mf.db"
)

cursor = connection.cursor()


# Query 1
print("\n" + "=" * 60)
print("QUERY 1: TOP 5 FUNDS BY AUM")
print("=" * 60)

cursor.execute("""
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)


# Query 2
print("\n" + "=" * 60)
print("QUERY 2: AVERAGE NAV PER MONTH")
print("=" * 60)

cursor.execute("""
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
""")

for row in cursor.fetchall():
    print(row)


# Query 3
print("\n" + "=" * 60)
print("QUERY 3: SIP INFLOW BY YEAR")
print("=" * 60)

cursor.execute("""
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_inflow
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;
""")

for row in cursor.fetchall():
    print(row)


# Query 4
print("\n" + "=" * 60)
print("QUERY 4: TRANSACTIONS BY STATE")
print("=" * 60)

cursor.execute("""
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;
""")

for row in cursor.fetchall():
    print(row)


# Query 5
print("\n" + "=" * 60)
print("QUERY 5: FUNDS WITH EXPENSE RATIO BELOW 1%")
print("=" * 60)

cursor.execute("""
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
""")

for row in cursor.fetchall():
    print(row)


# Query 6
print("\n" + "=" * 60)
print("QUERY 6: TOP 5 FUNDS BY 5-YEAR RETURN")
print("=" * 60)

cursor.execute("""
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)


# Query 7
print("\n" + "=" * 60)
print("QUERY 7: FUNDS WITH HIGH SHARPE RATIO")
print("=" * 60)

cursor.execute("""
SELECT
    scheme_name,
    sharpe_ratio,
    risk_grade
FROM fact_performance
WHERE sharpe_ratio > 1
ORDER BY sharpe_ratio DESC;
""")

for row in cursor.fetchall():
    print(row)


# Query 8
print("\n" + "=" * 60)
print("QUERY 8: AVERAGE TRANSACTION AMOUNT BY TYPE")
print("=" * 60)

cursor.execute("""
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    AVG(amount_inr) AS average_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY average_amount DESC;
""")

for row in cursor.fetchall():
    print(row)


# Query 9
print("\n" + "=" * 60)
print("QUERY 9: FUNDS BY RISK GRADE")
print("=" * 60)

cursor.execute("""
SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;
""")

for row in cursor.fetchall():
    print(row)


# Query 10
print("\n" + "=" * 60)
print("QUERY 10: FUNDS OUTPERFORMING BENCHMARK")
print("=" * 60)

cursor.execute("""
SELECT
    scheme_name,
    return_3yr_pct,
    benchmark_3yr_pct,
    alpha
FROM fact_performance
WHERE return_3yr_pct > benchmark_3yr_pct
ORDER BY alpha DESC
LIMIT 10;
""")

for row in cursor.fetchall():
    print(row)


connection.close()

print("\nAll 10 SQL queries executed successfully!")