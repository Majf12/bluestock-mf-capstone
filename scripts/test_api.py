import requests
import pandas as pd

scheme_code = "153665"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

nav_data = data["data"]

df = pd.DataFrame(nav_data)

df["scheme_code"] = scheme_code
df["scheme_name"] = data["meta"]["scheme_name"]

df.to_csv(
    "data/raw/sbi_nifty_nav_history.csv",
    index=False
)

print("NAV data saved successfully!")
print("Total records:", len(df))
print(df.head())