# This script checks the age of a file and alerts if it's older than 
# a specified threshold (in hours), useful for ensuring data freshness in pipelines.

import os
import time

def verify_freshness(filepath: str, max_hours=24):
    """
    Checks if a file is fresh; prints a warning if older than max_hours.
    """
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist.")
        return
    file_age_hours = (time.time() - os.path.getmtime(filepath)) / 3600
    if file_age_hours > max_hours:
        print(f"⚠️ WARNING: {filepath} is {file_age_hours:.1f} hours old and may be stale.")
    else:
        print(f"{filepath} is fresh (age: {file_age_hours:.1f} hours).")

# Example usage (assumes a file exists; you can use one of the generated CSVs above)
verify_freshness('sample_training_data.csv')
