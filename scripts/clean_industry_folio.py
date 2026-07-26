import pandas as pd
from pathlib import Path


# ============================================================
# INDUSTRY FOLIO COUNT DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("INDUSTRY FOLIO COUNT DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/06_industry_folio_count.csv"
)

folio_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(folio_df.shape)


# ------------------------------------------------------------
# 2. Convert month to datetime
# ------------------------------------------------------------

folio_df["month"] = pd.to_datetime(
    folio_df["month"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert folio columns to numeric
# ------------------------------------------------------------

numeric_columns = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]


for column in numeric_columns:

    folio_df[column] = pd.to_numeric(
        folio_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Check invalid negative folio counts
# ------------------------------------------------------------

invalid_folio_count = (
    folio_df[numeric_columns] < 0
).any(axis=1).sum()

print("\nInvalid Negative Folio Count:")
print(invalid_folio_count)


# ------------------------------------------------------------
# 5. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(folio_df.isnull().sum())


# ------------------------------------------------------------
# 6. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = folio_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 7. Remove duplicate rows
# ------------------------------------------------------------

folio_df = folio_df.drop_duplicates()


# ------------------------------------------------------------
# 8. Sort by month
# ------------------------------------------------------------

folio_df = folio_df.sort_values(
    by="month"
)


# ------------------------------------------------------------
# 9. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_industry_folio_count.csv"
)

folio_df.to_csv(
    output_path,
    index=False
)


print("\nClean Industry Folio data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(folio_df.shape)