import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Load investor transactions data
# --------------------------------------------------

input_file = Path(
    "data/raw/08_investor_transactions.csv"
)

transactions_df = pd.read_csv(
    input_file
)

print("\nColumn Names:")
print(transactions_df.columns.tolist())
# --------------------------------------------------
# 2. Standardise transaction_type
# --------------------------------------------------

transactions_df["transaction_type"] = (
    transactions_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)


# --------------------------------------------------
# 3. Validate transaction types
# --------------------------------------------------

valid_transaction_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_transaction_types = transactions_df[
    ~transactions_df["transaction_type"].isin(
        valid_transaction_types
    )
]


# --------------------------------------------------
# 4. Convert amount to numeric
# --------------------------------------------------

transactions_df["amount_inr"] = pd.to_numeric(
    transactions_df["amount_inr"],
    errors="coerce"
)


# --------------------------------------------------
# 5. Validate amount > 0
# --------------------------------------------------

invalid_amounts = transactions_df[
    transactions_df["amount_inr"] <= 0
]


# --------------------------------------------------
# 6. Check KYC status values
# --------------------------------------------------

print("\nUnique KYC Status Values:")
print(
    transactions_df["kyc_status"].unique()
)


# --------------------------------------------------
# 7. Convert date column
# --------------------------------------------------

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"],
    errors="coerce"
)


# --------------------------------------------------
# 8. Print validation results
# --------------------------------------------------

print("\n" + "=" * 60)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 60)

print("\nOriginal Shape:")
print(transactions_df.shape)

print("\nInvalid Transaction Type Count:")
print(len(invalid_transaction_types))

print("\nInvalid Amount Count:")
print(len(invalid_amounts))

print("\nMissing Values:")
print(transactions_df.isnull().sum())

print("\nDuplicate Rows:")
print(transactions_df.duplicated().sum())


# --------------------------------------------------
# 9. Remove duplicate rows
# --------------------------------------------------

transactions_df = transactions_df.drop_duplicates()


# --------------------------------------------------
# 10. Save cleaned data
# --------------------------------------------------

output_folder = Path(
    "data/processed"
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder / "clean_transactions.csv"
)

transactions_df.to_csv(
    output_file,
    index=False
)


print("\nClean transactions data saved successfully!")
print("Saved to:", output_file)