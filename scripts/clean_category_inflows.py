import pandas as pd
from pathlib import Path


# ============================================================
# CATEGORY INFLOWS DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("CATEGORY INFLOWS DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/05_category_inflows.csv"
)

category_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(category_df.shape)


# ------------------------------------------------------------
# 2. Convert month to datetime
# ------------------------------------------------------------

category_df["month"] = pd.to_datetime(
    category_df["month"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert net inflow to numeric
# ------------------------------------------------------------

category_df["net_inflow_crore"] = pd.to_numeric(
    category_df["net_inflow_crore"],
    errors="coerce"
)


# ------------------------------------------------------------
# 4. Check invalid dates
# ------------------------------------------------------------

invalid_date_count = category_df["month"].isna().sum()

print("\nInvalid Date Count:")
print(invalid_date_count)


# ------------------------------------------------------------
# 5. Check missing category values
# ------------------------------------------------------------

missing_category_count = category_df["category"].isna().sum()

print("\nMissing Category Count:")
print(missing_category_count)


# ------------------------------------------------------------
# 6. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(category_df.isnull().sum())


# ------------------------------------------------------------
# 7. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = category_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 8. Remove duplicate rows
# ------------------------------------------------------------

category_df = category_df.drop_duplicates()


# ------------------------------------------------------------
# 9. Sort by month and category
# ------------------------------------------------------------

category_df = category_df.sort_values(
    by=["month", "category"]
)


# ------------------------------------------------------------
# 10. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_category_inflows.csv"
)

category_df.to_csv(
    output_path,
    index=False
)


print("\nClean Category Inflows data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(category_df.shape)