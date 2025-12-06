import requests

API_KEY = "fca_live_lQbBeQE3EA2k8eBWFnjRJazkWd5yBgUsq1bWO6kL"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None


while True:
    base_currency = input("Enter the base currency (or 'Q' to quit): ").upper()
    if base_currency == "Q":
        break
    data = convert_currency(base_currency)
    if not data:
        continue
    del data[base_currency]
    for currency, rate in data.items():
        print(f"{currency}: {rate}")
