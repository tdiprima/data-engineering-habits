# This script defines a function to log metadata (lineage) for a Pandas DataFrame, 
# including source, creation time, row count, and columns. It appends this info to a 
# JSONL file and demonstrates usage with a sample CSV read.

import pandas as pd
import datetime
import json

def log_metadata(dataframe: pd.DataFrame, origin: str, log_file='metadata_log.jsonl'):
    """
    Logs metadata for the given DataFrame to a JSONL file.
    """
    metadata = {
        'origin': origin,
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'num_rows': len(dataframe),
        'column_names': list(dataframe.columns)
    }
    with open(log_file, 'a') as file:
        file.write(json.dumps(metadata) + '\n')
    return dataframe

# Example usage
# Generate a sample CSV if needed
sample_csv_content = """id,name,age
1,Alice,30
2,Bob,45
3,Charlie,25
"""
with open('sample_training_data.csv', 'w') as f:
    f.write(sample_csv_content)

df = pd.read_csv('sample_training_data.csv')
logged_df = log_metadata(df, 's3://mybucket/raw-data-2025/')
print("Logged metadata for DataFrame.")
