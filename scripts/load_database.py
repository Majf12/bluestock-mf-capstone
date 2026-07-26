import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


# --------------------------------------------------
# 1. Create SQLite database connection
# --------------------------------------------------

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)


# --------------------------------------------------
# 2. Load Fund Master
# --------------------------------------------------

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)


fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)


print("dim_fund table loaded successfully")


# --------------------------------------------------
# 3. Load Clean NAV Data
# --------------------------------------------------

clean_nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)


clean_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)


print("fact_nav table loaded successfully")


# --------------------------------------------------
# 4. Load Clean Transactions
# --------------------------------------------------

clean_transactions = pd.read_csv(
    "data/processed/clean_transactions.csv"
)


clean_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)


print("fact_transactions table loaded successfully")


# --------------------------------------------------
# 5. Load Clean Performance
# --------------------------------------------------

clean_performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)


clean_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)


print("fact_performance table loaded successfully")


print("\nAll cleaned data loaded into SQLite database!")
print("Database: bluestock_mf.db")