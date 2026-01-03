from datetime import datetime


def print_report(report):
    print("====== Weather Report ======")
    print(f"City: {report['city']}")
    print(f"Samples: {report['samples']}")

    if report['samples'] == 0:
        print("No data available for this city")
        return
    print("----------------------------")
    print(f"Min Temp: {report['min_temp']} °C")
    print(f"Max Temp: {report['max_temp']} °C")
    print(f"Avg Temp: {report['avg_temp']} °C")


def extract_temps(data):
    return [row["temp_c"] for row in data if "temp_c" in row]


def analyse_temps(temps):
    return {
        "min": min(temps),
        "max": max(temps),
        "average": round(sum(temps) / len(temps), 2)
    }


def filter_by_city(history, city):
    if not city:
        return history
    city_lower = city.strip().lower()
    return [row for row in history
            if str(row.get("city", "")).lower() == city_lower]


def extract_numbers(history, key):
    nums = []
    for row in history:
        value = row.get(key)
        if value is None:
            continue
        try:
            nums.append(float(value))
        except (TypeError, ValueError):
            continue
    return nums


def make_report(history, city=None, since=None):
    print("TIME", since)
    filtered = filter_by_city(history, city)
    if since:
        time_filtered = []
        for row in filtered:
            try:
                record_time = datetime.strptime(
                    row["time"], "%Y-%m-%d %H:%M")
                if record_time >= since:
                    time_filtered.append(row)
            except Exception:
                continue
        filtered = time_filtered
    else:
        since = None
    temps = extract_numbers(filtered, "temp_c")

    report_city = city if city else (
        filtered[-1].get("city") if filtered else "Unknown")

    if not temps:
        return {
            "city": report_city,
            "samples": 0,
            "min_temp": None,
            "max_temp": None,
            "avg_temp": None
        }

    return {
        "city": report_city,
        "samples": len(temps),
        "min_temp": min(temps),
        "max_temp": max(temps),
        "avg_temp": round(sum(temps) / len(temps), 2)
    }
