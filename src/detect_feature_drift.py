# This script uses the Kolmogorov-Smirnov test from SciPy to detect drift
# between two datasets by comparing feature distributions. It returns
# a list of drifted columns and demonstrates with sample old/new CSVs.

from pathlib import Path

import pandas as pd
from scipy.stats import ks_2samp


def check_drift(
    reference_data: pd.DataFrame, current_data: pd.DataFrame, p_threshold=0.1
):
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


# Example usage
old_df = pd.read_csv("../data/sample_old_data.csv")
new_df = pd.read_csv("../data/sample_new_data.csv")
drifted = check_drift(old_df, new_df)
print("Drifted columns:", drifted)
