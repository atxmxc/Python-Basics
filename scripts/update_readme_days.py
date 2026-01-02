from pathlib import Path
import re

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

marker = "<!-- AUTO-DAYS -->"

if marker not in text:
    raise SystemExit("AUTO-DAYS marker not found in README.md")

# find existing days in README
existing_days = set(
    int(n) for n in re.findall(r"\*\*Day(\d+)\*\*", text)
)

# find day folders
day_dirs = []
for p in Path(".").iterdir():
    if p.is_dir():
        m = re.match(r"day(\d+)", p.name, re.IGNORECASE)
        if m:
            day_dirs.append(int(m.group(1)))

day_dirs.sort()

# build lines for missing days only
new_lines = []
for day in day_dirs:
    if day not in existing_days:
        new_lines.append(f"- **Day{day:02d}** — _description pending_")

if not new_lines:
    print("No new days to add.")
    raise SystemExit

insert = "\n".join(new_lines) + "\n"

# insert before marker
updated = text.replace(marker, insert + "\n" + marker)
readme.write_text(updated, encoding="utf-8")

print(f"Added {len(new_lines)} new day(s) to README.")
