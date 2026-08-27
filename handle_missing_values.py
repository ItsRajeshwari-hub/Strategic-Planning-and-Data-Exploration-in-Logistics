"""
Step 2: Handle missing values using group-wise median imputation.
Input : cleaned_step1.csv
Output: cleaned_step2.csv
"""

import pandas as pd

df = pd.read_csv("cleaned_step1.csv", parse_dates=["promised_date", "actual_date"])

print("Missing values before imputation:")
print(df[["shipping_cost", "distance_km"]].isna().sum())

# Group-wise median imputation: fill missing cost/distance using the median
# for that destination_zone, since cost and distance vary systematically by region.
df["shipping_cost"] = df.groupby("destination_zone")["shipping_cost"].transform(
    lambda x: x.fillna(x.median())
)

df["distance_km"] = df.groupby("destination_zone")["distance_km"].transform(
    lambda x: x.fillna(x.median())
)

print("\nMissing values after imputation:")
print(df[["shipping_cost", "distance_km"]].isna().sum())

df.to_csv("cleaned_step2.csv", index=False)
print("Saved -> cleaned_step2.csv")
