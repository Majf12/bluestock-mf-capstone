import pandas as pd
from pathlib import Path


# ============================================================
# FUND MASTER DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("FUND MASTER DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------

input_path = Path("data/raw/01_fund_master.csv")

fund_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(fund_df.shape)


# ------------------------------------------------------------
# 2. Convert launch_date to datetime
# ------------------------------------------------------------

fund_df["launch_date"] = pd.to_datetime(
    fund_df["launch_date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "amfi_code",
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]


for column in numeric_columns:

    fund_df[column] = pd.to_numeric(
        fund_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Check duplicate AMFI codes
# ------------------------------------------------------------

duplicate_amfi_codes = fund_df["amfi_code"].duplicated().sum()

print("\nDuplicate AMFI Code Count:")
print(duplicate_amfi_codes)


# ------------------------------------------------------------
# 5. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = fund_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 6. Check invalid expense ratios
# ------------------------------------------------------------

invalid_expense_ratio = (
    (fund_df["expense_ratio_pct"] < 0) |
    (fund_df["expense_ratio_pct"] > 10)
).sum()

print("\nInvalid Expense Ratio Count:")
print(invalid_expense_ratio)


# ------------------------------------------------------------
# 7. Check invalid exit loads
# ------------------------------------------------------------

invalid_exit_load = (
    (fund_df["exit_load_pct"] < 0) |
    (fund_df["exit_load_pct"] > 10)
).sum()

print("\nInvalid Exit Load Count:")
print(invalid_exit_load)


# ------------------------------------------------------------
# 8. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(fund_df.isnull().sum())


# ------------------------------------------------------------
# 9. Remove duplicate rows
# ------------------------------------------------------------

fund_df = fund_df.drop_duplicates()


# ------------------------------------------------------------
# 10. Sort by AMFI code
# ------------------------------------------------------------

fund_df = fund_df.sort_values(
    by="amfi_code"
)


# ------------------------------------------------------------
# 11. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_fund_master.csv"
)

fund_df.to_csv(
    output_path,
    index=False
)


print("\nClean Fund Master data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(fund_df.shape)