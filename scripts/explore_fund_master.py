import pandas as pd

# Fund Master dataset load
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)


# 1. Unique Fund Houses
print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(fund_master["fund_house"].nunique())


# 2. Unique Categories
print("\nUnique Categories:")
print(fund_master["category"].unique())


# 3. Unique Sub-Categories
print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())


# 4. Unique Risk Categories
print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())


# 5. AMFI Scheme Codes
print("\nAMFI Scheme Codes:")
print(fund_master["amfi_code"].head(10))


print("\n" + "=" * 60)
print("Fund Master exploration completed!")
print("=" * 60)

# Task 7: AMFI Code Validation
# --------------------------------------------------

# Fund Master AMFI codes
fund_codes = set(
    fund_master["amfi_code"]
)

# NAV History dataset load
nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

# NAV History AMFI codes
nav_codes = set(
    nav_history["amfi_code"]
)

# Fund Master have but nav history have no codes
missing_codes = fund_codes - nav_codes


print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print("\nTotal Fund Master Codes:")
print(len(fund_codes))

print("\nTotal NAV History Codes:")
print(len(nav_codes))

print("\nMissing Codes:")
print(missing_codes)

if len(missing_codes) == 0:
    print("\nResult:")
    print("All AMFI codes in fund_master exist in nav_history.")
else:
    print("\nResult:")
    print("Some AMFI codes are missing in nav_history.")