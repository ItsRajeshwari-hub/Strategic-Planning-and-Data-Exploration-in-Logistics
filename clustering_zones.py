from sklearn.cluster import KMeans

zone_features = orders.groupby('zone_id').agg(
    avg_distance=('distance_km', 'mean'),
    order_volume=('order_id', 'count'),
    avg_delay=('delay_hours', 'mean')
).reset_index()

kmeans = KMeans(n_clusters=4, random_state=42)
zone_features['cluster'] = kmeans.fit_predict(
    zone_features[['avg_distance', 'order_volume', 'avg_delay']]
)
