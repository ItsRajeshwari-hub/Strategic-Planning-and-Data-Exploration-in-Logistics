import pandas as pd

# Load raw logistics data
orders = pd.read_csv('orders.csv', parse_dates=['promised_date', 'actual_date'])

# Clean: drop duplicates, handle missing timestamps
orders = orders.drop_duplicates(subset='order_id')
orders = orders.dropna(subset=['actual_date'])

# Derived KPI field: delivery delay in hours
orders['delay_hours'] = (orders['actual_date'] - orders['promised_date']).dt.total_seconds() / 3600
orders['on_time'] = orders['delay_hours'] <= 0
