# This script defines a function to log metadata (lineage) for a Pandas DataFrame,
# including source, creation time, row count, and columns. It appends this info to a
# JSONL file and demonstrates usage with a sample CSV read.

import datetime
import json
from pathlib import Path

import pandas as pd


def log_metadata(dataframe: pd.DataFrame, origin: str, log_file="metadata_log.jsonl"):
    """
    Logs metadata for the given DataFrame to a JSONL file.
    """
    metadata = {
        "origin": origin,
        "timestamp": datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
        "num_rows": len(dataframe),
        "column_names": list(dataframe.columns),
    }
    log_path = Path(log_file)
    log_content = json.dumps(metadata) + "\n"
    if log_path.exists():
        log_content = log_path.read_text() + log_content
    log_path.write_text(log_content)
    return dataframe


# Example usage
df = pd.read_csv("../data/sample_training_data.csv")
logged_df = log_metadata(df, "s3://mybucket/raw-data-2025/")
print("Logged metadata for DataFrame.")
