"""
Step 4: Normalize numeric fields using Min-Max scaling.
Input : cleaned_step3.csv
Output: cleaned_step4.csv
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("cleaned_step3.csv", parse_dates=["promised_date", "actual_date"])

numeric_cols = ["distance_km", "order_weight_kg", "shipping_cost", "inventory_level"]

print("Before normalization:")
print(df[numeric_cols].describe().loc[["min", "max"]])

scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\nAfter normalization (all values scaled to 0-1):")
print(df[numeric_cols].describe().loc[["min", "max"]])

df.to_csv("cleaned_step4.csv", index=False)
print("Saved -> cleaned_step4.csv")
