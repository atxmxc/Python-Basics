import json
import requests
from pathlib import Path


def write_to_json(filename, weather):
    path = Path(filename)

    if path.exists():
        with path.open('r', encoding='utf-8') as f:
            try:
                datas = json.load(f)
            except json.JSONDecodeError:
                datas = []
    else:
        datas = []

    if isinstance(datas, dict):
        datas = [datas]
    datas.append(weather)

    with open("forecast.json", "w", encoding="utf-8") as f:
        json.dump(datas, f, indent=2)


def write_to_log(filename):
    with open("api.log", "a", encoding="utf-8") as e:
        e.write(f"API HAS SUCCESSFULLY TRANSMITTED DATA.\n")


url = "https://api.open-meteo.com/v1/forecast"

lat = float(input("Please Enter The Latitude of The Location: "))
long = float(input("Please Enter The Longitude of The Location "))


params = {
    "latitude": lat,
    "longitude": long,
    "current_weather": True
}
print(params)
try:
    response = requests.get(url, params=params, timeout=5)

    if response.status_code == 200:
        data = response.json()
        weather = data['current_weather']
        print(data)
        write_to_json("forecast.json", weather)
        write_to_log("api.log")
    else:
        print(f"API ERROR CODE: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Network Error: {e}")
