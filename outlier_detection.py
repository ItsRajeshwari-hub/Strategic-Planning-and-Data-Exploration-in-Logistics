"""
Step 3: Detect and treat outliers using the Interquartile Range (IQR) method.
Input : cleaned_step2.csv
Output: cleaned_step3.csv
"""

import pandas as pd

df = pd.read_csv("cleaned_step2.csv", parse_dates=["promised_date", "actual_date"])


def cap_outliers_iqr(series):
    """Cap values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR] instead of dropping them,
    preserving the record while limiting the influence of extreme values."""
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return series.clip(lower=lower, upper=upper)


print("Distance stats before capping:")
print(df["distance_km"].describe()[["min", "max"]])

df["distance_km"] = cap_outliers_iqr(df["distance_km"])
df["shipping_cost"] = cap_outliers_iqr(df["shipping_cost"])

print("\nDistance stats after capping:")
print(df["distance_km"].describe()[["min", "max"]])

# Remove clearly invalid entries (e.g., negative distance from data-entry errors)
before = len(df)
df = df[df["distance_km"] >= 0]
print(f"\nRemoved {before - len(df)} record(s) with invalid negative distance")

df.to_csv("cleaned_step3.csv", index=False)
print("Saved -> cleaned_step3.csv")
