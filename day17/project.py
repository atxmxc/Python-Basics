import os
import requests
import json
import argparse
import pathlib as Path
print("API_KEY from env:", os.getenv("API_KEY"))

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Missing Environmental Variable")
    raise SystemExit

parser = argparse.ArgumentParser()
parser.add_argument("--city", required=True)
args = parser.parse_args()

url = "https://api.weatherapi.com/v1/current.json"
params = {
    "q": args.city,
    "key": API_KEY,
    "units": "metric"
}
r = requests.get(url, params=params, timeout=5)
if r.status_code == 200:
    data = r.json()
    print(f"Temp: {data['current']['temp_c']}")
else:
    print(f"Error: {r.status_code},{r.text}")
