# This script demonstrates prototyping an ETL process by sampling a small
# fraction (1%) of a large dataset for quick testing and iteration, using
# Pandas for reading and sampling.

from pathlib import Path

import pandas as pd

# Load and sample
full_df = pd.read_csv("../data/large_sample_dataset.csv")
sampled_df = full_df.sample(frac=0.01, random_state=42)
print(f"Sampled DataFrame shape: {sampled_df.shape}")

# Example ETL transformations on the sampled data
# 1. Data Cleaning: Remove any rows with missing values
cleaned_df = sampled_df.dropna()

# 2. Transformation: Create a new feature (e.g., value_squared)
cleaned_df["value_squared"] = cleaned_df["value"] ** 2

# 3. Transformation: Normalize the 'value' column to 0-1 range
min_val = cleaned_df["value"].min()
max_val = cleaned_df["value"].max()
cleaned_df["value_normalized"] = (cleaned_df["value"] - min_val) / (max_val - min_val)

# 4. Filtering: Keep only rows where id is even
filtered_df = cleaned_df[cleaned_df["id"] % 2 == 0]

print(f"\nAfter ETL transformations:")
print(f"  - Rows after cleaning: {len(cleaned_df)}")
print(f"  - Rows after filtering: {len(filtered_df)}")
print(f"  - New columns added: {list(filtered_df.columns)}")
print(f"\nSample of transformed data:")
print(filtered_df.head())
