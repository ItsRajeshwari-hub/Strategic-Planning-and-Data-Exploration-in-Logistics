import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("cleaned_final.csv", parse_dates=["promised_date", "actual_date"])
df["delay_days"] = (df["actual_date"] - df["promised_date"]).dt.days

# ---------- Problem Definition ----------
# Target: delay_days (continuous) -- how many days late (0 or negative-ish clipped) a delivery is
# Features: distance_km, order_weight_kg, shipping_cost, inventory_level (numeric)
#           destination_zone, origin_warehouse (categorical)
features_num = ["distance_km", "order_weight_kg", "shipping_cost", "inventory_level"]
features_cat = ["destination_zone", "origin_warehouse"]
target = "delay_days"

X = df[features_num + features_cat]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), features_cat),
    ],
    remainder="passthrough",
)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=4, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42),
}

results = []
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    pipe = Pipeline([("prep", preprocessor), ("model", model)])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    cv_scores = cross_val_score(pipe, X, y, cv=kfold, scoring="neg_root_mean_squared_error")
    cv_rmse_mean = -cv_scores.mean()
    cv_rmse_std = cv_scores.std()

    results.append({
        "model": name, "test_rmse": rmse, "test_mae": mae, "test_r2": r2,
        "cv_rmse_mean": cv_rmse_mean, "cv_rmse_std": cv_rmse_std,
    })
    print(f"\n=== {name} ===")
    print(f"Test RMSE: {rmse:.3f} | Test MAE: {mae:.3f} | Test R2: {r2:.3f}")
    print(f"5-fold CV RMSE: {cv_rmse_mean:.3f} (+/- {cv_rmse_std:.3f})")

results_df = pd.DataFrame(results)
results_df.to_csv("model_results.csv", index=False)
print("\n\nSummary table:")
print(results_df.round(3))

# ---------- Feature importance from Random Forest (best interpretable ensemble) ----------
rf_pipe = Pipeline([("prep", preprocessor), ("model", RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42))])
rf_pipe.fit(X_train, y_train)

ohe = rf_pipe.named_steps["prep"].named_transformers_["cat"]
cat_names = list(ohe.get_feature_names_out(features_cat))
all_feature_names = cat_names + features_num

importances = rf_pipe.named_steps["model"].feature_importances_
fi = pd.DataFrame({"feature": all_feature_names, "importance": importances}).sort_values("importance", ascending=False)
fi.to_csv("feature_importance.csv", index=False)
print("\nTop feature importances (Random Forest):")
print(fi.head(8).round(3))
