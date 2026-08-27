"""
Step 5: Standardize inconsistent categorical text formatting.
Input : cleaned_step4.csv
Output: cleaned_final.csv
"""

import pandas as pd

df = pd.read_csv("cleaned_step4.csv", parse_dates=["promised_date", "actual_date"])

print("Warehouse names before standardization:")
print(df["origin_warehouse"].unique())

# Standardize to a consistent lowercase, underscore-separated format so that
# labels like 'Warehouse A' and 'warehouse_a' are treated as the same category.
df["origin_warehouse"] = (
    df["origin_warehouse"].str.strip().str.lower().str.replace(" ", "_")
)

print("\nWarehouse names after standardization:")
print(df["origin_warehouse"].unique())

df.to_csv("cleaned_final.csv", index=False)
print("Saved -> cleaned_final.csv (fully cleaned & preprocessed dataset)")
