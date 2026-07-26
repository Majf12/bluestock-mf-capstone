import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. Set raw data folder
# --------------------------------------------------

raw_folder = Path("data/raw")


# --------------------------------------------------
# 2. Find all original CSV datasets
# --------------------------------------------------

csv_files = [
    file for file in raw_folder.glob("*.csv")
    if file.name.startswith(tuple(str(i).zfill(2) for i in range(1, 11)))
]


# --------------------------------------------------
# 3. Load and inspect each CSV dataset
# --------------------------------------------------

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    # Load CSV file
    df = pd.read_csv(file)

    # Print shape
    print("\nShape:")
    print(df.shape)

    # Print data types
    print("\nData Types:")
    print(df.dtypes)

    # Print first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

    # Print missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Print duplicate rows
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

print("\n" + "=" * 60)
print("All 10 CSV datasets loaded and inspected successfully!")
print("=" * 60)

