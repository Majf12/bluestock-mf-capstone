import pandas as pd
from pathlib import Path


# ============================================================
# AUM BY FUND HOUSE DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("AUM BY FUND HOUSE DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/03_aum_by_fund_house.csv"
)

aum_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(aum_df.shape)


# ------------------------------------------------------------
# 2. Convert date column to datetime
# ------------------------------------------------------------

aum_df["date"] = pd.to_datetime(
    aum_df["date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]


for column in numeric_columns:

    aum_df[column] = pd.to_numeric(
        aum_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Check invalid AUM values
# ------------------------------------------------------------

invalid_aum_count = (
    (aum_df["aum_lakh_crore"] < 0) |
    (aum_df["aum_crore"] < 0)
).sum()

print("\nInvalid AUM Count:")
print(invalid_aum_count)


# ------------------------------------------------------------
# 5. Check invalid number of schemes
# ------------------------------------------------------------

invalid_scheme_count = (
    aum_df["num_schemes"] <= 0
).sum()

print("\nInvalid Number of Schemes:")
print(invalid_scheme_count)


# ------------------------------------------------------------
# 6. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(aum_df.isnull().sum())


# ------------------------------------------------------------
# 7. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = aum_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 8. Remove duplicate rows
# ------------------------------------------------------------

aum_df = aum_df.drop_duplicates()


# ------------------------------------------------------------
# 9. Sort data
# ------------------------------------------------------------

aum_df = aum_df.sort_values(
    by=["date", "fund_house"]
)


# ------------------------------------------------------------
# 10. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_aum_by_fund_house.csv"
)

aum_df.to_csv(
    output_path,
    index=False
)


print("\nClean AUM data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(aum_df.shape)