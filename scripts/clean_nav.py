import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Load NAV history data
# --------------------------------------------------

input_file = Path("data/raw/02_nav_history.csv")

nav_df = pd.read_csv(
    input_file
)


# --------------------------------------------------
# 2. Convert date column to datetime
# --------------------------------------------------

nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    errors="coerce"
)


# --------------------------------------------------
# 3. Convert NAV column to numeric
# --------------------------------------------------

nav_df["nav"] = pd.to_numeric(
    nav_df["nav"],
    errors="coerce"
)


# --------------------------------------------------
# 4. Sort by AMFI code and date
# --------------------------------------------------

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)


# --------------------------------------------------
# 5. Forward-fill missing NAV values
# --------------------------------------------------

nav_df["nav"] = (
    nav_df
    .groupby("amfi_code")["nav"]
    .ffill()
)


# --------------------------------------------------
# 6. Remove duplicate rows
# --------------------------------------------------

nav_df = nav_df.drop_duplicates()


# --------------------------------------------------
# 7. Validate NAV values
# --------------------------------------------------

invalid_nav = nav_df[
    nav_df["nav"] <= 0
]


print("\n" + "=" * 60)
print("NAV DATA CLEANING")
print("=" * 60)

print("\nFinal Shape:")
print(nav_df.shape)

print("\nMissing Values:")
print(nav_df.isnull().sum())

print("\nInvalid NAV Count:")
print(len(invalid_nav))

print("\nDuplicate Rows:")
print(nav_df.duplicated().sum())


# --------------------------------------------------
# 8. Save cleaned data
# --------------------------------------------------

output_folder = Path("data/processed")

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder / "clean_nav.csv"
)

nav_df.to_csv(
    output_file,
    index=False
)


print("\nClean NAV data saved successfully!")
print("Saved to:", output_file)