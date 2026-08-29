import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 150

# ---------- Reproduce cleaned dataset (from Week 2 pipeline) ----------
df = pd.read_csv("logistics_orders.csv", parse_dates=["promised_date", "actual_date"])
df = df.drop_duplicates(subset="order_id")
df = df.dropna(subset=["order_id", "actual_date"])

df["shipping_cost"] = df.groupby("destination_zone")["shipping_cost"].transform(lambda x: x.fillna(x.median()))
df["distance_km"] = df.groupby("destination_zone")["distance_km"].transform(lambda x: x.fillna(x.median()))

def cap_outliers_iqr(series):
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return series.clip(lower=lower, upper=upper)

df["distance_km"] = cap_outliers_iqr(df["distance_km"])
df["shipping_cost"] = cap_outliers_iqr(df["shipping_cost"])
df = df[df["distance_km"] >= 0]

df["origin_warehouse"] = df["origin_warehouse"].str.strip().str.lower().str.replace(" ", "_")

# Derived field: delivery delay in days
df["delay_days"] = (df["actual_date"] - df["promised_date"]).dt.days

df.to_csv("cleaned_final.csv", index=False)

# ---------- EDA: central tendency, distribution, correlation ----------
numeric_cols = ["distance_km", "order_weight_kg", "shipping_cost", "inventory_level", "delay_days"]
summary = df[numeric_cols].describe().T
summary.to_csv("eda_summary_stats.csv")
print("=== Summary statistics ===")
print(summary[["mean", "50%", "std", "min", "max"]])

corr = df[numeric_cols].corr()
print("\n=== Correlation matrix ===")
print(corr.round(2))

# ---------- Visualization 1: Distribution of delivery distance ----------
plt.figure(figsize=(7, 4.5))
sns.histplot(df["distance_km"], bins=20, kde=True, color="#1F4E5C")
plt.title("Distribution of Delivery Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("chart1_distance_distribution.png")
plt.close()

# ---------- Visualization 2: Average shipping cost by destination zone ----------
zone_cost = df.groupby("destination_zone")["shipping_cost"].mean().sort_values(ascending=False)
plt.figure(figsize=(7, 4.5))
sns.barplot(x=zone_cost.index, y=zone_cost.values, color="#2E7D8C")
plt.title("Average Shipping Cost by Destination Zone")
plt.xlabel("Destination Zone")
plt.ylabel("Average Shipping Cost")
plt.tight_layout()
plt.savefig("chart2_avg_cost_by_zone.png")
plt.close()

# ---------- Visualization 3: Distance vs Shipping Cost (scatter) ----------
plt.figure(figsize=(7, 4.5))
sns.scatterplot(data=df, x="distance_km", y="shipping_cost", hue="destination_zone", palette="viridis", s=45)
plt.title("Relationship Between Distance and Shipping Cost")
plt.xlabel("Distance (km)")
plt.ylabel("Shipping Cost")
plt.legend(title="Zone", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
plt.tight_layout()
plt.savefig("chart3_distance_vs_cost.png")
plt.close()

# ---------- Visualization 4: Correlation heatmap ----------
plt.figure(figsize=(6.5, 5))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", square=True, cbar_kws={"shrink": 0.8})
plt.title("Correlation Between Key Logistics Variables")
plt.tight_layout()
plt.savefig("chart4_correlation_heatmap.png")
plt.close()

# ---------- Visualization 5: Delivery delay by warehouse (boxplot) ----------
plt.figure(figsize=(7, 4.5))
sns.boxplot(data=df, x="origin_warehouse", y="delay_days", color="#7FB3BE")
plt.title("Delivery Delay Distribution by Warehouse")
plt.xlabel("Origin Warehouse")
plt.ylabel("Delay (days)")
plt.tight_layout()
plt.savefig("chart5_delay_by_warehouse.png")
plt.close()

print("\nAll charts saved successfully.")
