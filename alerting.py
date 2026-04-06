def send_alert(anomalies):
    for index, row in anomalies.iterrows():
        print(f"ALERT: Query {row['query_id']} is anomalous. Execution time: {row['execution_time']}s")
