import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")

csv_files = list(raw_folder.glob("*.csv"))

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values by Column:")
    print(df.isnull().sum())

    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # Missing values உள்ள file-ன் rows மட்டும் பார்க்க
    if df.isnull().sum().sum() > 0:

        print("\nRows with Missing Values:")
        print(
            df[df.isnull().any(axis=1)].to_string(index=False)
        )

