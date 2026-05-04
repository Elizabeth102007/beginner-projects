import requests
BASE_URL = "https://api.coingecko.com/api/v3/simple/price/"


def get_price():
    params = {
        "ids" : "bitcoin",
        "vs_currencies" : "usd",
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        price_usd = data["bitcoin"]["usd"]
        return price_usd
    except requests.exceptions.RequestException as e:
        print("API request failed", e)
        return None



from datetime import date
import csv

import os

file_path = "prices.csv"


def save_to_csv(coin, price_usd) :
    today = date.today().isoformat()

    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["date", "coin", "price_usd"])

        writer.writerow([today, coin, price_usd])

save_to_csv("Bitcoin", get_price())
def main():
    price_usd = get_price()
    if price_usd:
        save_to_csv("Bitcoin", price_usd)
        print(f"{date.today()} | Bitcoin | ${price_usd} saved")

if __name__ == "__main__":
    main()






