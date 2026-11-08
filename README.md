# Attendance Tracker

A small command-line tool to record and summarise member attendance for a team or association.

## Why I built it

As a member of the HR team of a student association, I tracked attendance by hand. This tool records presence, lateness and absences, then calculates attendance rates automatically, which saves time and avoids counting mistakes.

## Features

- Add an attendance record (present, late or absent) for a member on a given date
- Summary table with each member's counts and attendance rate
- "Star of the week": the member with the best attendance over the last 7 days
- Data stored in a simple CSV file that can be opened in Excel

## How to run

You need Python 3.8 or later. No extra libraries are required.

```bash
python attendance_tracker.py
```

Then pick an option from the menu. Records are saved in `attendance.csv` (created automatically). A sample file, `sample_attendance.csv`, is included so you can see the format; copy it to `attendance.csv` to try the summary.

## How it works

- Each record has three fields: `date`, `name`, `status`
- The attendance rate is `(present + late) / total sessions`
- The star of the week is chosen by fewest absences, then fewest late arrivals, then most presences

## Possible improvements

- Edit or delete a record
- Export the summary to Excel
- Graphical interface or web version
- Monthly reports

## Tech

Python 3 (standard library only: `csv`, `os`, `datetime`)
