import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Fund Master Data Loaded Successfully!")

print("\n1. Shape:")
print(df.shape)

print("\n2. Missing Values:")
print(df.isnull().sum())

print("\n3. Duplicate Rows:")
print(df.duplicated().sum())

print("\n4. Duplicate AMFI Codes:")
print(df["amfi_code"].duplicated().sum())

print("\n5. Data Types:")
print(df.dtypes)