import requests
import pandas as pd
from pathlib import Path

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

output_folder = Path("data/raw")

for scheme_name, scheme_code in schemes.items():

    print("\n" + "=" * 60)
    print(f"Fetching: {scheme_name}")
    print(f"Scheme Code: {scheme_code}")
    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("API request failed!")
        continue

    data = response.json()

    print("API Scheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    nav_df["scheme_code"] = scheme_code

    nav_df["date"] = pd.to_datetime(
        nav_df["date"],
        format="%d-%m-%Y"
    )

    nav_df["nav"] = pd.to_numeric(nav_df["nav"])

    print("\nFirst 5 NAV Records:")
    print(nav_df.head())

    print("\nShape:", nav_df.shape)

    output_path = output_folder / f"{scheme_name}_live_nav.csv"

    nav_df.to_csv(output_path, index=False)

    print("Saved:", output_path)

print("\nAll selected scheme NAV data fetched successfully!")