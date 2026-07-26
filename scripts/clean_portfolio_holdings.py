import pandas as pd
from pathlib import Path


# ============================================================
# PORTFOLIO HOLDINGS DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("PORTFOLIO HOLDINGS DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/09_portfolio_holdings.csv"
)

holdings_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(holdings_df.shape)


# ------------------------------------------------------------
# 2. Convert date column to datetime
# ------------------------------------------------------------

holdings_df["portfolio_date"] = pd.to_datetime(
    holdings_df["portfolio_date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "amfi_code",
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]


for column in numeric_columns:

    holdings_df[column] = pd.to_numeric(
        holdings_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Check invalid weight percentages
# ------------------------------------------------------------

invalid_weight_count = (
    (holdings_df["weight_pct"] < 0) |
    (holdings_df["weight_pct"] > 100)
).sum()

print("\nInvalid Weight Percentage Count:")
print(invalid_weight_count)


# ------------------------------------------------------------
# 5. Check invalid market values and prices
# ------------------------------------------------------------

invalid_value_count = (
    (holdings_df["market_value_cr"] < 0) |
    (holdings_df["current_price_inr"] < 0)
).sum()

print("\nInvalid Market Value / Price Count:")
print(invalid_value_count)


# ------------------------------------------------------------
# 6. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(holdings_df.isnull().sum())


# ------------------------------------------------------------
# 7. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = holdings_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 8. Remove duplicate rows
# ------------------------------------------------------------

holdings_df = holdings_df.drop_duplicates()


# ------------------------------------------------------------
# 9. Sort data
# ------------------------------------------------------------

holdings_df = holdings_df.sort_values(
    by=["amfi_code", "portfolio_date"]
)


# ------------------------------------------------------------
# 10. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_portfolio_holdings.csv"
)

holdings_df.to_csv(
    output_path,
    index=False
)


print("\nClean Portfolio Holdings data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(holdings_df.shape)