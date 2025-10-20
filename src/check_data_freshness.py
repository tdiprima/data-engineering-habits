# This script checks the age of a file and alerts if it's older than
# a specified threshold (in hours), useful for ensuring data freshness in pipelines.

import time
from pathlib import Path


def verify_freshness(filepath: str, max_hours=24):
    """
    Checks if a file is fresh; prints a warning if older than max_hours.
    """
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File {filepath} does not exist.")
        return
    file_age_hours = (time.time() - path.stat().st_mtime) / 3600
    if file_age_hours > max_hours:
        print(
            f"⚠️ WARNING: {filepath} is {file_age_hours:.1f} hours old and may be stale."
        )
    else:
        print(f"{filepath} is fresh (age: {file_age_hours:.1f} hours).")


# Example usage
verify_freshness("../data/sample_training_data.csv")
