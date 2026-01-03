import os
import requests


def fetch_weather(city):
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Missing API_KEY env")
        raise SystemExit

    url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        "key": api_key,
        "q": city
    }

    r = requests.get(url, params=params, timeout=5)
    return r
