# day19 project; a mixture of json history, usiung pathlib and extracting
import json
from pathlib import Path


def load_history(filename="day18/history.json"):
    path = Path(filename)
    if not path.exists():
        print("No history.json found.")
        return []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Invalid JSON.")
        return []


def extract_temps(data):
    return [row["temp_c"] for row in data if "temp_c" in row]


def analyse_temps(temps):
    return {
        "min": min(temps),
        "max": max(temps),
        "average": round(sum(temps) / len(temps), 2)
    }


def print_report(city, stats, count):
    print("====== Weather Report ======")
    print(f"City: {city}")
    print(f"Samples: {count}")
    print("----------------------------")
    print(f"Min Temp: {stats['min']} °C")
    print(f"Max Temp: {stats['max']} °C")
    print(f"Avg Temp: {stats['average']} °C")


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
