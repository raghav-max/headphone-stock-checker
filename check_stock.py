import requests
import os

URL = "https://www.headphonezone.in/products/hifiman-arya-stealth-magnet-version.json"
URL2 = "https://www.headphonezone.in/products/topping-dx5-ii.json"

USER_KEY = os.getenv("PUSHOVER_USER_KEY")
API_TOKEN = os.getenv("PUSHOVER_API_TOKEN")

def notify(msg):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": API_TOKEN,
            "user": USER_KEY,
            "message": msg,
            "title": "Headphone Restock Alert",
            "priority": 2,
            "retry": 60,
            "expire": 3600,
            "sound": "alien"
        }
    )

def check_stock_dac():
    r = requests.get(URL2)
    r.raise_for_status()

    data = r.json()
    variants = data["product"]["variants"]

    for v in variants:
        print(v)
        qty = v["inventory_quantity"]

        if qty > 0:
            notify(
                "🚨 Topping DX5 II is in stock!\n"
                "https://www.headphonezone.in/products/topping-dx5-ii"
            )
            print("🚨 IN STOCK")
            print("https://www.headphonezone.in/products/topping-dx5-ii")
            return

    print("❌ Still sold out")

def check_stock_headphone():
    r = requests.get(URL)
    r.raise_for_status()

    data = r.json()
    variants = data["product"]["variants"]

    for v in variants:
        print(v)
        qty = v["inventory_quantity"]

        if qty > 0:
            notify(
                "🚨 Arya Stealth is in stock!\n"
                "https://www.headphonezone.in/products/hifiman-arya-stealth-magnet-version"
            )
            print("🚨 IN STOCK")
            print("https://www.headphonezone.in/products/hifiman-arya-stealth-magnet-version")
            return

    print("❌ Still sold out")

if __name__ == "__main__":
    check_stock_headphone()
    check_stock_dac()
