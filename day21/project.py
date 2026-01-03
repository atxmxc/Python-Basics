# imports
import os
import json
import requests
import argparse
import csv
from pathlib import Path
from datetime import datetime, timedelta
from reporting import make_report, print_report
from storage import load_history, export_csv, append_history
from api_client import fetch_weather
from logger import log_api


def parse_since(since_str):
    number_part = since_str[:-1]
    unit = since_str[-1]

    amount = int(number_part)
    now = datetime.now()

    if unit == "m":
        return now - timedelta(minutes=amount)
    elif unit == "h":
        return now - timedelta(hours=amount)
    elif unit == "d":
        return now - timedelta(days=amount)


# parser config
parser = argparse.ArgumentParser()
parser.add_argument(
    "--city", help="City Name, (only used when using --save, to filter using --report)")
parser.add_argument("--save", action="store_true")
parser.add_argument("--export", action="store_true")
parser.add_argument("--report", action="store_true")
parser.add_argument(
    "--since", help="choose the timeframe to create the report")
args = parser.parse_args()

if args.since and not args.report:
    print("You must use --report with --since")
    raise SystemExit


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
    history = load_history()

    if args.since:
        cutoff = parse_since(args.since)
    else:
        cutoff = None

    report = make_report(history, city=args.city, since=cutoff)
    print_report(report)
    raise SystemExit


else:
    parser.print_help()
