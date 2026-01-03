from datetime import datetime
# log api funcction


def log_api(message):
    with open("day21/api.log", "a", encoding="utf-8") as f:
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        f.write(f"{date}: {message}\n")
