import requests

search_name = "SBI Bluechip"

url = "https://api.mfapi.in/mf/search"

response = requests.get(
    url,
    params={"q": search_name}
)

print("Status Code:", response.status_code)

data = response.json()

print("\nSearch Results:")

for scheme in data:
    print(scheme)