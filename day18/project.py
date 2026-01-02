import argparse
import json
from pathlib import Path
from datetime import datetime
import csv
import os
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--city")
parser.add_argument("--save", action="store_true")
parser.add_argument("--export", action="store_true")
args = parser.parse_args()


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("day18/api.log", "a", encoding="utf-8") as f:
        f.write(f"{timestamp}: {message}\n")


def append_history(entry, filename="day18/history.json"):
    path = Path(filename)

    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8") or "[]")
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    if isinstance(data, dict):
        data = [data]

    data.append(entry)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def export_csv(filename_json="day18/history.json", filename_csv="day18/weather.csv"):
    path = Path(filename_json)
    if not path.exists():
        print("File History Not Found.")
        return

    data = json.loads(path.read_text(encoding="utf-8") or "[]")
    if not data:
        print("History is Empty")
        return

    fields = sorted({k for row in data for k in row.keys()})

    with open(filename_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    print(f"Exported {len(data)} rows to {filename_csv}")


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


if args.export:
    export_csv()
    raise SystemExit

if args.save:
    if not args.city:
        print("Provide --city when using --save")
        raise SystemExit

    r = fetch_weather(args.city)

    if r.status_code == 200:
        data = r.json()
        entry = {
            "city": data['location']['name'],
            "country": data['location']['country'],
            "time": data['location']['localtime'],
            "temp_c": data['current']['temp_c'],
            "wind_kph": data['current']['wind_kph'],
            "humidity": data['current']['humidity'],
            "condition": data['current']['condition']['text']
        }
        append_history(entry)
        log(f"SAVE OK city={args.city} temp_c={entry['temp_c']}")
        print("Saved to history.json")

    else:
        log(f"SAVE FAIL city={args.city} status={r.status_code}")
        print(f"API ERROR: {r.status_code}")
        print(r.text)

else:
    parser.print_help()
