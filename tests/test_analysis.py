from analysis import load_data, filter_data, summary

def test_summary_chicago_sample():
    # Uses the tiny sample you added earlier
    df = load_data("chicago.csv")
    # Try a filter that returns >=0 rows (could be 0; function must stay robust)
    df_jan = filter_data(df, month="January", day="Sunday")
    s = summary(df_jan)
    # Basic shape checks
    assert set(s.keys()) == {"rows", "trip_duration_total", "trip_duration_mean", "most_common_start_station"}
    assert s["rows"] >= 0
    assert s["trip_duration_total"] >= 0.0
    assert s["trip_duration_mean"] >= 0.0
