import requests

import os

BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city, api_key):
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def display_weather(data) :
    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

def main():
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("API key not found. Set WEATHER_API_KEY.")
        return

    city = input("Enter city: ")

    try:
        data = get_weather(city, api_key)
        display_weather(data)
    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 400:
            print("Invalid city name.")
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    main()









