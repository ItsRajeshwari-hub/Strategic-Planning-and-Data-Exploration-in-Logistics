# Strategic-Planning-and-Data-Exploration-in-Logistics
Strategic planning and data exploration for a logistics operation using Python  includes data cleaning, regression-based delay prediction, delivery zone clustering, and route optimization.
Scenario

A mid-size e-commerce fulfillment operation managing regional warehouses and a last-mile delivery fleet, facing challenges with on-time delivery, inventory allocation, and transportation costs.

Files

`data_cleaning.py` — Loads and cleans raw order data, derives a delivery delay KPI field.
`regression_delay_prediction.py` — Linear regression model to predict delivery delay based on distance, weight, day of week, and warehouse load.
`clustering_zones.py` — K-Means clustering to segment delivery zones by distance, order volume, and delay.
`route_optimization.py` — Simplified nearest-neighbor route sequencing illustration (conceptually extendable to a full Vehicle Routing Problem solver).

Key Performance Indicators (KPIs)

1. On-Time Delivery Rate (OTD)
2. Inventory Turnover Ratio
3. Average Cost per Delivery
4. Order Fulfillment Cycle Time




## Week 2 Files. Data Cleaning & Preprocessing

`logistics_orders.csv`. This sample simulated dataset is used as the input for the data cleaning & preprocessing pipeline. It contains missing values, outliers and duplicate records for demonstration purposes.

 `load_and_deduplicate.py`. This script loads the raw dataset removes duplicate records and drops rows that lack essential identifiers. It is the step in the data cleaning & preprocessing workflow.

 `handle_missing_values.py`. This script fills missing cost and distance values by using a group- median imputation that is based on the delivery zone. It follows the step.

 `outlier_detection.py`. This script. Caps outliers in the distance and cost fields, by applying the IQR method. It is the stage of the data cleaning & preprocessing process.

 `normalization.py`. This script scales numeric fields to a range of 0 to 1 using Min–Max normalization. It continues the data cleaning & preprocessing chain.

 `standardize_categorical.py`. This script standardises inconsistent warehouse name formatting to ensure uniformity across the dataset. It completes the data cleaning & preprocessing sequence.

Each script reads the output of the step and writes its own output file forming a sequential data cleaning & preprocessing pipeline: `load_and_deduplicate.py` → `handle_missing_values.py` → `outlier_detection.py` → `normalization.py` → `standardize_categorical.py`.

## Week 3 Task: Advanced Data Analysis and Visualization in Logistics

This report shows a look at the data we worked on for the logistics project. We did this analysis over the two weeks using the data that was cleaned and prepared in week two. We looked at some numbers like how far the deliveries are, how heavy the orders are, how much it costs to ship how much stock is in the warehouse and a new number we created called delivery delay. We checked how these numbers are related to each other and what they tell us.

We made five pictures using tools in Python like matplotlib and seaborn. Each picture helps us see things. One picture shows how far deliveries usually are another compares how much it costs to ship to places another looks at how distance and cost are connected another shows how all the numbers are related and the last one compares how long it takes to deliver from different warehouses.

What we found is clear. The cost to ship is mostly because of how the delivery is and that connection is pretty strong. The weight of the order also has some effect on the cost. The time it takes to deliver is not really connected to how it is. Instead it looks like some warehouses are doing better than others. One warehouse had more variation, in how long it took to deliver and that was easy to see in the picture we made.

The website where we put all our work has the code we used to make the pictures and the pictures themselves. That way anyone can check the work again. All the numbers and pictures help us make suggestions for making the logistics work better.
