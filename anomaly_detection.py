from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[['execution_time', 'bytes_scanned']])
    return df[df['anomaly'] == -1]
