import pandas as pd
from pathlib import Path


# ============================================================
# MONTHLY SIP INFLOWS DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("MONTHLY SIP INFLOWS DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(sip_df.shape)


# ------------------------------------------------------------
# 2. Convert month to datetime
# ------------------------------------------------------------

sip_df["month"] = pd.to_datetime(
    sip_df["month"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]


for column in numeric_columns:

    sip_df[column] = pd.to_numeric(
        sip_df[column],
        errors="coerce"
    )


# ------------------------------------------------------------
# 4. Check invalid negative values
# ------------------------------------------------------------

invalid_inflow_count = (
    sip_df["sip_inflow_crore"] < 0
).sum()

print("\nInvalid SIP Inflow Count:")
print(invalid_inflow_count)


invalid_account_count = (
    (sip_df["active_sip_accounts_crore"] < 0) |
    (sip_df["new_sip_accounts_lakh"] < 0) |
    (sip_df["sip_aum_lakh_crore"] < 0)
).sum()

print("\nInvalid Account/AUM Count:")
print(invalid_account_count)


# ------------------------------------------------------------
# 5. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(sip_df.isnull().sum())


# ------------------------------------------------------------
# 6. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = sip_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 7. Remove duplicate rows
# ------------------------------------------------------------

sip_df = sip_df.drop_duplicates()


# ------------------------------------------------------------
# 8. Sort by month
# ------------------------------------------------------------

sip_df = sip_df.sort_values(
    by="month"
)


# ------------------------------------------------------------
# 9. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_monthly_sip_inflows.csv"
)

sip_df.to_csv(
    output_path,
    index=False
)


print("\nClean SIP inflows data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(sip_df.shape)