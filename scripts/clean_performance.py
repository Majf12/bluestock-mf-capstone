import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Load scheme performance data
# --------------------------------------------------

input_file = Path(
    "data/raw/07_scheme_performance.csv"
)

performance_df = pd.read_csv(
    input_file
)


# --------------------------------------------------
# 2. Performance columns
# --------------------------------------------------

performance_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]


# --------------------------------------------------
# 3. Convert performance columns to numeric
# --------------------------------------------------

for column in performance_columns:

    performance_df[column] = pd.to_numeric(
        performance_df[column],
        errors="coerce"
    )


# --------------------------------------------------
# 4. Flag negative Sharpe ratios
# --------------------------------------------------

negative_sharpe = performance_df[
    performance_df["sharpe_ratio"] < 0
]


# --------------------------------------------------
# 5. Validate expense ratio range
# --------------------------------------------------

invalid_expense_ratio = performance_df[
    (performance_df["expense_ratio_pct"] < 0.1)
    |
    (performance_df["expense_ratio_pct"] > 2.5)
]


# --------------------------------------------------
# 6. Check missing values
# --------------------------------------------------

missing_values = performance_df.isnull().sum()


# --------------------------------------------------
# 7. Remove duplicate rows
# --------------------------------------------------

performance_df = performance_df.drop_duplicates()


# --------------------------------------------------
# 8. Print validation results
# --------------------------------------------------

print("\n" + "=" * 60)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 60)

print("\nOriginal Shape:")
print(performance_df.shape)

print("\nNegative Sharpe Ratio Count:")
print(len(negative_sharpe))

print("\nInvalid Expense Ratio Count:")
print(len(invalid_expense_ratio))

print("\nMissing Values:")
print(missing_values)

print("\nDuplicate Rows:")
print(performance_df.duplicated().sum())


# --------------------------------------------------
# 9. Save cleaned data
# --------------------------------------------------

output_folder = Path(
    "data/processed"
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder / "clean_performance.csv"
)

performance_df.to_csv(
    output_file,
    index=False
)


print("\nClean performance data saved successfully!")
print("Saved to:", output_file)