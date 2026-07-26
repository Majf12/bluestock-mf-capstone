import pandas as pd
from pathlib import Path


# ============================================================
# BENCHMARK INDICES DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("BENCHMARK INDICES DATA CLEANING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

input_path = Path(
    "data/raw/10_benchmark_indices.csv"
)

benchmark_df = pd.read_csv(input_path)


print("\nOriginal Shape:")
print(benchmark_df.shape)


# ------------------------------------------------------------
# 2. Convert date column to datetime
# ------------------------------------------------------------

benchmark_df["date"] = pd.to_datetime(
    benchmark_df["date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert close value to numeric
# ------------------------------------------------------------

benchmark_df["close_value"] = pd.to_numeric(
    benchmark_df["close_value"],
    errors="coerce"
)


# ------------------------------------------------------------
# 4. Check invalid dates
# ------------------------------------------------------------

invalid_date_count = (
    benchmark_df["date"].isna()
).sum()

print("\nInvalid Date Count:")
print(invalid_date_count)


# ------------------------------------------------------------
# 5. Check invalid close values
# ------------------------------------------------------------

invalid_close_value_count = (
    benchmark_df["close_value"] <= 0
).sum()

print("\nInvalid Close Value Count:")
print(invalid_close_value_count)


# ------------------------------------------------------------
# 6. Check missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(benchmark_df.isnull().sum())


# ------------------------------------------------------------
# 7. Check duplicate rows
# ------------------------------------------------------------

duplicate_rows = benchmark_df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)


# ------------------------------------------------------------
# 8. Remove duplicate rows
# ------------------------------------------------------------

benchmark_df = benchmark_df.drop_duplicates()


# ------------------------------------------------------------
# 9. Sort data
# ------------------------------------------------------------

benchmark_df = benchmark_df.sort_values(
    by=["index_name", "date"]
)


# ------------------------------------------------------------
# 10. Save cleaned data
# ------------------------------------------------------------

output_path = Path(
    "data/processed/clean_benchmark_indices.csv"
)

benchmark_df.to_csv(
    output_path,
    index=False
)


print("\nClean Benchmark Indices data saved successfully!")
print("Saved to:", output_path)


print("\nFinal Shape:")
print(benchmark_df.shape)