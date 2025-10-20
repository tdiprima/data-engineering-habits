# This script registers dataset metadata (ID, name, description, path)
# into a JSONL catalog file using UUID for unique IDs. It includes an example registration.

import json
import uuid


def add_to_catalog(
    dataset_name: str, desc: str, location: str, catalog_file="data_catalog.jsonl"
):
    """
    Registers dataset info to a JSONL catalog.
    """
    info = {
        "unique_id": str(uuid.uuid4()),
        "dataset_name": dataset_name,
        "description": desc,
        "storage_path": location,
    }
    with open(catalog_file, "a") as file:
        file.write(json.dumps(info) + "\n")
    print(f"Registered: {dataset_name}")


# Example usage
add_to_catalog(
    "user_interactions",
    "Processed logs of user events",
    "s3://data-lake/clean/user_events/",
)
