# analysis.py
import pandas as pd

def load_data(city_csv: str) -> pd.DataFrame:
    df = pd.read_csv(city_csv, parse_dates=["Start Time", "End Time"])
    # Add convenience columns for filters; robust if someone passes month/day later
    df["month_name"] = df["Start Time"].dt.month_name()
    df["day_name"] = df["Start Time"].dt.day_name()
    return df

def filter_data(df: pd.DataFrame, month: str | None = None, day: str | None = None) -> pd.DataFrame:
    out = df
    if month and month.lower() != "all":
        out = out[out["month_name"].str.lower() == month.lower()]
    if day and day.lower() != "all":
        out = out[out["day_name"].str.lower() == day.lower()]
    return out

def summary(df: pd.DataFrame) -> dict:
    """Return tiny summary; safe on empty frames and missing columns."""
    n = int(len(df))
    total = float(df["Trip Duration"].sum()) if "Trip Duration" in df and n else 0.0
    mean = float(df["Trip Duration"].mean()) if "Trip Duration" in df and n else 0.0
    start_station = None
    if n and "Start Station" in df and not df["Start Station"].empty:
        try:
            start_station = df["Start Station"].mode().iat[0]
        except Exception:
            start_station = None
    return {"rows": n, "trip_duration_total": total, "trip_duration_mean": mean, "most_common_start_station": start_station}
