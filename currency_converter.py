import requests

# API endpoint
url = "https://api.exchangerate-api.com/v4/latest/"

# user input
base = input("Enter base currency (e.g. USD): ").upper()
target = input("Enter target currency (e.g. INR): ").upper()
amount = float(input("Enter amount: "))

# fetch data
response = requests.get(url + base)
data = response.json()

if target in data["rates"]:
    rate = data["rates"][target]
    result = amount * rate
    print(f"\n{amount} {base} = {result:.2f} {target}")
    print(f"(1 {base} = {rate:.2f} {target})")
else:
    print("Invalid target currency")