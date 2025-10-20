# This script demonstrates prototyping an ETL process by sampling a small
# fraction (1%) of a large dataset for quick testing and iteration, using
# Pandas for reading and sampling.

from pathlib import Path

import pandas as pd

# Generate a sample large CSV if needed
# This simulates a "huge" dataset with 100 rows; scale as needed.
large_csv_content = "id,value\n" + "\n".join(f"{i},{i*2.5}" for i in range(100))
Path("large_sample_dataset.csv").write_text(large_csv_content)

# Load and sample
full_df = pd.read_csv("large_sample_dataset.csv")
sampled_df = full_df.sample(frac=0.01, random_state=42)
print(f"Sampled DataFrame shape: {sampled_df.shape}")
# Now prototype your ETL on sampled_df (e.g., transformations, cleaning)
