import pandas as pd

df = pd.read_csv('logistics_orders.csv', parse_dates=['promised_date', 'actual_date'])

# Remove duplicate order records
df = df.drop_duplicates(subset='order_id')

# Drop records missing essential identifiers
df = df.dropna(subset=['order_id', 'actual_date'])
