# Bikeshare Analysis — Git & Pandas Mini-Project

[![CI](https://github.com/andigles/pdsnd_github/actions/workflows/ci.yml/badge.svg)](https://github.com/andigles/pdsnd_github/actions/workflows/ci.yml)

**Scope:** Fork of a Udacity project to practice **Git/GitHub**. I turned it into a small, **reproducible** demo: tiny sample CSV files, a tested non-interactive analysis (`analysis.py`), and **CI** (continuous integration) with GitHub Actions that runs tests on every push.

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
