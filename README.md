# Strategic-Planning-and-Data-Exploration-in-Logistics
Strategic planning and data exploration for a logistics operation using Python  includes data cleaning, regression-based delay prediction, delivery zone clustering, and route optimization.
## Scenario

A mid-size e-commerce fulfillment operation managing regional warehouses and a last-mile delivery fleet, facing challenges with on-time delivery, inventory allocation, and transportation costs.

## Files

- `data_cleaning.py` — Loads and cleans raw order data, derives a delivery delay KPI field.
- `regression_delay_prediction.py` — Linear regression model to predict delivery delay based on distance, weight, day of week, and warehouse load.
- `clustering_zones.py` — K-Means clustering to segment delivery zones by distance, order volume, and delay.
- `route_optimization.py` — Simplified nearest-neighbor route sequencing illustration (conceptually extendable to a full Vehicle Routing Problem solver).

## Key Performance Indicators (KPIs)

1. On-Time Delivery Rate (OTD)
2. Inventory Turnover Ratio
3. Average Cost per Delivery
4. Order Fulfillment Cycle Time
