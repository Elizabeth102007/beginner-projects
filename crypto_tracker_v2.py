import requests
import csv
import os
from datetime import date, datetime

# -------------------------------
# Configuration
# -------------------------------
COINS = ["bitcoin", "ethereum", "ripple", "solana", "tether"]
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
CSV_FILE = "crypto_prices.csv"


# -------------------------------
# Functions
# -------------------------------

def get_price(coin):
    """Fetch the current USD price for a coin from CoinGecko"""
    params = {
        "ids": coin,
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data[coin]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {coin} price: {e}")
        return None


def save_to_csv(coin, price_usd):
    """Save the coin price to CSV if not already saved today"""
    today = date.today().isoformat()
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check if file exists
    file_exists = os.path.exists(CSV_FILE)

    # Read existing entries to prevent duplicate
    existing_entries = set()
    if file_exists:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if row and row[0] == today and row[2].lower() == coin:
                    existing_entries.add(coin.lower())

    # Only write if coin not already saved today
    if coin.lower() not in existing_entries:
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["date", "time", "coin", "price_usd"])
            writer.writerow([today, current_time, coin, price_usd])
        print(f"Saved {coin} price: ${price_usd}")
    else:
        print(f"{coin} price already saved for today.")


# -------------------------------
# Main orchestration
# -------------------------------
def main():
    for coin in COINS:
        price = get_price(coin)
        if price is not None:
            save_to_csv(coin, price)


if __name__ == "__main__":
    main()
