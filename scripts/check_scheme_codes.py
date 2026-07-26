import pandas as pd

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

selected_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

selected_funds = fund_master[
    fund_master["amfi_code"].isin(selected_codes)
]

print(selected_funds[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category"
    ]
].to_string(index=False))