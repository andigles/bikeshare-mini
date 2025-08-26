# Bikeshare Analysis — Git & Pandas Mini-Project

[![CI](https://github.com/andigles/bikeshare-mini/actions/workflows/ci.yml/badge.svg)](https://github.com/andigles/bikeshare-mini/actions/workflows/ci.yml)

**Scope:** Fork of a Udacity project to practice **Git/GitHub**. I turned it into a small, **reproducible** demo: tiny sample CSV files, a tested non‑interactive analysis (`analysis.py`), and **CI** (continuous integration) with GitHub Actions that runs tests on every push.

---

## What this shows (in one line)
A simple **CLI** (command-line interface) friendly analysis that reads bikeshare trips and computes basic stats by city/month/day using pandas.

---

## Quickstart (runs in minutes)

> Prerequisite: Python 3.10+ installed.

```bash
# 1) (optional) create & activate a virtual environment
python -m venv .venv
# Windows Git Bash:
source .venv/Scripts/activate
# Windows PowerShell:
# .\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# 2) install dependencies and run the tests
pip install -r requirements.txt
pytest -q

# 3) (optional) run the original interactive script from the course
python bikeshare.py
```

---

## Tiny proof (deterministic output from the sample data)

```bash
python - <<'PY'
import json, analysis as A
s = A.summary(A.filter_data(A.load_data("chicago.csv"), month="January", day="Sunday"))
print(json.dumps(s, indent=2))
PY
```

Expected from the included 3-row sample:

```json
{
  "rows": 1,
  "trip_duration_total": 776.0,
  "trip_duration_mean": 776.0,
  "most_common_start_station": "Streeter Dr & Grand Ave"
}
```

---

## Project structure

```
.
├── analysis.py                 # tiny, testable analysis: load -> optional filter -> summary
├── bikeshare.py                # original interactive script from the course
├── chicago.csv                 # tiny 3-row sample (for instant runs)
├── new_york_city.csv           # tiny 3-row sample
├── washington.csv              # tiny 3-row sample (no Gender/Birth Year columns by design)
├── requirements.txt
├── tests/
│   ├── conftest.py             # ensures repo root is importable during tests
│   └── test_analysis.py        # “happy-path” test for the sample data
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions workflow (CI)
```

**Note on data:** Place any large/full datasets under `data/` (this folder is git‑ignored) using the same filenames if you want to run on complete data locally.

---

## How the analysis works

- `load_data(city_csv)`: reads a CSV, parses dates, and adds `month_name` / `day_name`.
- `filter_data(df, month, day)`: optional filters by month/day (case-insensitive; `"all"` keeps everything).
- `summary(df)`: returns a small dictionary with:
  - `rows`: number of rows after filtering  
  - `trip_duration_total`: total trip time in seconds  
  - `trip_duration_mean`: mean trip time in seconds  
  - `most_common_start_station`: mode of the start station (if present)

---

## Continuous Integration (CI)

This repo uses **GitHub Actions** to run `pytest` automatically on every push and pull request.  
The badge at the top links to the latest run. A green badge means a fresh clone can run the code and tests without manual tweaks.

---

## Why this repo exists

This started as an **Udacity “Introduction to Version Control”** exercise focused on Git/GitHub basics.  
I kept it as a clean, reproducible demo to show:
- good repository hygiene (README, tests, CI, license),
- tiny but real pandas analysis with deterministic sample data,
- instant “clone → run → see results” experience.

---

## Troubleshooting

- **`ModuleNotFoundError` during tests**: ensure tests add the repo root to the import path (handled by `tests/conftest.py`) and that `analysis.py` is at the repo root.
- **CSV not found**: make sure the tiny sample files are present at the repo root (`chicago.csv`, `new_york_city.csv`, `washington.csv`). Large files should live in `data/` (git‑ignored).

---

## License

MIT — see `LICENSE`.

---

## Acknowledgments

- Based on the Udacity **Programming for Data Science with Python** bikeshare project scaffold.  
- Adapted and extended by @andigles to add reproducible analysis, tests, and CI.
