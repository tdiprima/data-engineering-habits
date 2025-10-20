# ML Data Engineering Habits

![Personal Repo](https://img.shields.io/badge/🔒-personal_repo-blueviolet?style=for-the-badge)

This repository contains Python scripts and a shell script demonstrating key data engineering habits for successful projects, based on best practices for data handling, validation, versioning, and monitoring.

## Files
- `log_data_lineage.py`: Logs DataFrame metadata for traceability.
- `validate_data_schema.py`: Validates DataFrame schema and constraints.
- `version_data_with_dvc.sh`: Shell script for versioning datasets with DVC.
- `detect_feature_drift.py`: Detects data drift using statistical tests.
- `prototype_etl_sampling.py`: Samples large datasets for quick ETL prototyping.
- `register_data_catalog.py`: Registers datasets in a metadata catalog.
- `check_data_freshness.py`: Checks file freshness for data observability.

## Usage
Run each script individually with Python (or bash for the shell script).  
Requires Git and DVC for versioning.

## Installation
Use uv to install dependencies:

```sh
uv add pandas pandera scipy dvc
# or
uv sync
```
