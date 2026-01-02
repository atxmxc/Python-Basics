# using api's(keys, rate limits and real data)
# api key is a unique key for yourself and its sent with each request
# there are multiple ways to send a key but ill use this one for today
import requests
import json
# params = {
#     "key": API,
#     "q": "London"
# }


url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 51.5072,
    "longitude": -0.1276,
    "current_weather": True
}

try:
    response = requests.get(url, params=params, timeout=5)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        print("Temperature:", weather["temperature"])
        print("Wind speed:", weather["windspeed"])
        with open("for.json", "w", encoding="utf-8") as e:
            json.dump(weather['windspeed'], e, indent=2)
    else:
        print("API error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Network error:", e)
# we can also store the data from the api into an external file.
with open("forecast.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
