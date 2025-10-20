# This script uses the Kolmogorov-Smirnov test from SciPy to detect drift 
# between two datasets by comparing feature distributions. It returns 
# a list of drifted columns and demonstrates with sample old/new CSVs.

from scipy.stats import ks_2samp
import pandas as pd

def check_drift(reference_data: pd.DataFrame, current_data: pd.DataFrame, p_threshold=0.1):
    """
    Detects drifted features using KS-test.
    """
    drifted_cols = []
    for col in reference_data.columns:
        if col in current_data.columns:  # Ensure column exists in both
            stat, p_value = ks_2samp(reference_data[col], current_data[col])
            if p_value < p_threshold:
                drifted_cols.append(col)
    return drifted_cols

# Generate sample CSVs if needed
# sample_old_data.csv (2024 data)
old_csv_content = """feature1,feature2
10,20.5
15,25.0
12,22.0
"""
with open('sample_old_data.csv', 'w') as f:
    f.write(old_csv_content)

# sample_new_data.csv (2025 data with slight drift)
new_csv_content = """feature1,feature2
11,21.0
16,26.5
13,23.5
"""
with open('sample_new_data.csv', 'w') as f:
    f.write(new_csv_content)

# Example usage
old_df = pd.read_csv('sample_old_data.csv')
new_df = pd.read_csv('sample_new_data.csv')
drifted = check_drift(old_df, new_df)
print("Drifted columns:", drifted)
