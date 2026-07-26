import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv",
    parse_dates=["date"]
)

print("NAV History Data Loaded Successfully!")

print("\nShape of the data:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nNumber of NAV records per fund:")
print(df["amfi_code"].value_counts().head(10))

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

print("Funds in Fund Master:", fund_master["amfi_code"].nunique())

print(
    "Funds in NAV History:",
    nav_history["amfi_code"].nunique()
)