# imports
import os
import json
import requests
import argparse
import csv
from pathlib import Path
from datetime import datetime

# parser config
parser = argparse.ArgumentParser()
parser.add_argument("--city")
parser.add_argument("--save", action="store_true")
parser.add_argument("--export", action="store_true")
parser.add_argument("--report", action="store_true")
args = parser.parse_args()

# fetch weather function


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

# append history function


def append_history(entry, filename="day20/history.json"):
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

# export csv function


def export_csv(filename_json="day20/history.json", filename_csv="day20/weather.csv"):
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

# log api funcction


def log_api(message):
    with open("day20/api.log", "a", encoding="utf-8") as f:
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f.write(f"{date}: {message}\n")

# extract temps function


def extract_temps(data):
    return [row["temp_c"] for row in data if "temp_c" in row]

# analyse temps function


def analyse_temps(temps):
    return {
        "min": min(temps),
        "max": max(temps),
        "average": round(sum(temps) / len(temps), 2)
    }

# print report function


def print_report(city, stats, count):
    print("====== Weather Report ======")
    print(f"City: {city}")
    print(f"Samples: {count}")
    print("----------------------------")
    print(f"Min Temp: {stats['min']} °C")
    print(f"Max Temp: {stats['max']} °C")
    print(f"Avg Temp: {stats['average']} °C")

# load history function


def load_history(filename="day20/history.json"):
    path = Path(filename)
    if not path.exists():
        print("No history.json found.")
        return []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Invalid JSON.")
        return []


# main logic
if args.export:
    export_csv()

elif args.save:
    if not args.city:
        print("You Must Use --city if you want to save")
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
        log_api("API SUCCESSFULLY FETCHED, PARSED AND EXPORTED DATA")
        print("Saved To history.json")

    else:
        print("Failed To Save To history.json")
        log_api("API FAILED TO FETCH, PARSE AND EXPORT DATA")
        print(f"API ERROR: {r.status_code}")
        print(r.text)

elif args.report:
    data = load_history()

    if not data:
        raise SystemExit

    temps = extract_temps(data)

    if not temps:
        print("No temperature data found.")
        raise SystemExit

    stats = analyse_temps(temps)
    city = data[-1].get("city", "Unknown")

    print_report(city, stats, len(temps))

else:
    parser.print_help()
