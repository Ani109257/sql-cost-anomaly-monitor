
import pandas as pd

def load_query_logs(file_path):
    df = pd.read_csv(file_path)
    # Basic preprocessing
    df['execution_time'] = pd.to_numeric(df['execution_time'], errors='coerce')
    df = df.dropna()
    return df
