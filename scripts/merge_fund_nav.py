import pandas as pd

# Fund Master data-வை load செய்கிறோம்
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# NAV History data-வை load செய்கிறோம்
nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv",
    parse_dates=["date"]
)

# amfi_code மூலம் இரண்டு datasets-ஐ merge செய்கிறோம்
merged_df = pd.merge(
    nav_history,
    fund_master,
    on="amfi_code",
    how="left"
)

print("Data merged successfully!")

print("\nMerged data shape:")
print(merged_df.shape)

print("\nMerged columns:")
print(merged_df.columns.tolist())

print("\nFirst 5 rows:")
print(merged_df.head())

merged_df.to_csv(
    "data/processed/fund_nav_combined.csv",
    index=False
)

print("\nCombined data saved successfully!")

# ஒவ்வொரு fund-க்கும் first மற்றும் last NAV கண்டுபிடிக்கிறோம்
fund_returns = (
    merged_df
    .sort_values(["amfi_code", "date"])
    .groupby("amfi_code")
    .agg(
        first_nav=("nav", "first"),
        last_nav=("nav", "last"),
        start_date=("date", "first"),
        end_date=("date", "last"),
        scheme_name=("scheme_name", "first"),
        category=("category", "first"),
        risk_category=("risk_category", "first")
    )
    .reset_index()
)

# Return percentage calculate செய்கிறோம்
fund_returns["return_pct"] = (
    (fund_returns["last_nav"] - fund_returns["first_nav"])
    / fund_returns["first_nav"]
) * 100

print("\nFund Returns:")
print(fund_returns.head())

fund_returns["years"] = (
    (fund_returns["end_date"] - fund_returns["start_date"])
    .dt.days / 365.25
)

print("\nFund Return Period:")
print(
    fund_returns[
        ["amfi_code", "start_date", "end_date", "years"]
    ].head()
)

fund_returns["cagr_pct"] = (
    (
        fund_returns["last_nav"]
        / fund_returns["first_nav"]
    )
    ** (1 / fund_returns["years"])
    - 1
) * 100

print("\nFund Returns with CAGR:")
print(
    fund_returns[
        [
            "amfi_code",
            "scheme_name",
            "return_pct",
            "years",
            "cagr_pct"
        ]
    ].head()
)

top_10_funds = fund_returns.sort_values(
    by="cagr_pct",
    ascending=False
).head(10)

print("\nTop 10 Funds by CAGR:")
print(
    top_10_funds[
        [
            "amfi_code",
            "scheme_name",
            "category",
            "risk_category",
            "cagr_pct"
        ]
    ]
)

top_10_funds = top_10_funds.copy()

top_10_funds["rank"] = range(1, len(top_10_funds) + 1)

top_10_funds = top_10_funds[
    [
        "rank",
        "amfi_code",
        "scheme_name",
        "category",
        "risk_category",
        "cagr_pct"
    ]
]

print("\nTop 10 Funds by CAGR:")
print(top_10_funds.to_string(index=False))

top_10_funds.to_csv(
    "data/processed/top_10_funds_by_cagr.csv",
    index=False
)

print("\nTop 10 funds saved successfully!")

category_performance = (
    fund_returns
    .groupby("category")
    .agg(
        average_cagr_pct=("cagr_pct", "mean"),
        number_of_funds=("amfi_code", "nunique")
    )
    .reset_index()
)

category_performance = category_performance.sort_values(
    by="average_cagr_pct",
    ascending=False
)

print("\nCategory-wise Performance:")
print(
    category_performance.to_string(index=False)
)

risk_performance = (
    fund_returns
    .groupby("risk_category")
    .agg(
        average_cagr_pct=("cagr_pct", "mean"),
        number_of_funds=("amfi_code", "nunique")
    )
    .reset_index()
)

risk_performance = risk_performance.sort_values(
    by="average_cagr_pct",
    ascending=False
)

print("\nRisk-wise Performance:")
print(
    risk_performance.to_string(index=False)
)

category_performance.to_csv(
    "data/processed/category_performance.csv",
    index=False
)

risk_performance.to_csv(
    "data/processed/risk_performance.csv",
    index=False
)

print("\nCategory and risk performance files saved successfully!")