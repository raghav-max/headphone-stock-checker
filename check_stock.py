import requests

URL = "https://www.headphonezone.in/products/hifiman-arya-stealth-magnet-version.json"

def check_stock():
    r = requests.get(URL)
    r.raise_for_status()

    data = r.json()
    variants = data["product"]["variants"]

    for v in variants:
        print(v)
        qty = v["inventory_quantity"]

        if qty > 0:
            print("🚨 IN STOCK")
            print("https://www.headphonezone.in/products/hifiman-arya-stealth-magnet-version")
            return

    print("❌ Still sold out")

if __name__ == "__main__":
    check_stock()
