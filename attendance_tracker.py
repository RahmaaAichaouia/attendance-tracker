"""Attendance Tracker: record and summarise member attendance (CSV storage)."""

import csv
import os
from datetime import date, timedelta

FILE = "attendance.csv"
FIELDS = ["date", "name", "status"]
STATUSES = {"1": "present", "2": "late", "3": "absent"}


def load_records():
    """Read all records from the CSV file (empty list if it doesn't exist)."""
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_record(day, name, status):
    """Append one record to the CSV file, creating it with a header if needed."""
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({"date": day, "name": name, "status": status})


def add_record():
    """Ask the user for a name, a status and a date, then save it."""
    name = input("Member name: ").strip().title()
    print("1) present   2) late   3) absent")
    choice = input("Status: ").strip()
    if not name or choice not in STATUSES:
        print("Invalid input, nothing saved.")
        return
    day = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
    day = day or str(date.today())
    save_record(day, name, STATUSES[choice])
    print("Saved.")


def compute_stats(records):
    """Count present / late / absent for each member."""
    stats = {}
    for r in records:
        member = stats.setdefault(r["name"], {"present": 0, "late": 0, "absent": 0})
        member[r["status"]] += 1
    return stats


def attendance_rate(counts):
    """Percentage of sessions attended (a late arrival still counts as attended)."""
    total = sum(counts.values())
    return (counts["present"] + counts["late"]) / total * 100


def show_summary():
    """Print a table with each member's counts and attendance rate."""
    stats = compute_stats(load_records())
    if not stats:
        print("No records yet.")
        return
    print(f"\n{'Name':<15}{'Present':>8}{'Late':>6}{'Absent':>8}{'Rate':>8}")
    for name, c in sorted(stats.items()):
        print(f"{name:<15}{c['present']:>8}{c['late']:>6}{c['absent']:>8}"
              f"{attendance_rate(c):>7.0f}%")


def star_of_the_week():
    """Best member over the last 7 days: fewest absences, then fewest lates."""
    since = str(date.today() - timedelta(days=7))
    recent = [r for r in load_records() if r["date"] >= since]
    stats = compute_stats(recent)
    if not stats:
        print("No records in the last 7 days.")
        return
    best = max(stats, key=lambda n: (-stats[n]["absent"], -stats[n]["late"],
                                     stats[n]["present"]))
    print(f"\nStar of the week: {best}")


def main():
    while True:
        print("\n=== Attendance Tracker ===")
        print("1) Add a record")
        print("2) Show summary")
        print("3) Star of the week")
        print("4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_record()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            star_of_the_week()
        elif choice == "4":
            break
        else:
            print("Please choose 1-4.")


if __name__ == "__main__":
    main()
