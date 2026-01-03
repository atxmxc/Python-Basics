import json
import csv
from pathlib import Path


def append_history(entry, filename="day21/history.json"):
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


def export_csv(filename_json="day21/history.json", filename_csv="day21/weather.csv"):
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


def load_history(filename="day21/history.json"):
    path = Path(filename)
    if not path.exists():
        print("No history.json found.")
        return []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Invalid JSON.")
        return []
