# Data Engineering Workflow Guide

This guide walks you through the proper order to execute the scripts in this repository, following data engineering best practices. Each script represents a critical habit for maintaining reliable, production-ready ML data pipelines.

## Workflow Overview

```
1. Prototype → 2. Validate → 3. Version → 4. Register → 5. Log → 6. Monitor → 7. Detect Drift
```

## Step 1: Prototype Your ETL with Sampling

**Script:** `src/prototype_etl_sampling.py`

**Why First?**  
Before working with production-scale data, always prototype your ETL logic on a small sample. This allows rapid iteration without waiting for full data processing.

**What It Does:**

- Samples 1% of a large dataset (`data/large_sample_dataset.csv`)
- Demonstrates ETL transformations: cleaning, feature engineering, filtering
- Shows the results of your transformations quickly

**Run:**

```bash
python src/prototype_etl_sampling.py
```

**Best Practice:**  
Iterate on your data transformation logic here until you're confident it works correctly. Only then scale to full data.

## Step 2: Validate Data Schema

**Script:** `src/validate_data_schema.py`

**Why Second?**  
Once your ETL logic is solid, validate that your data conforms to expected schemas. This catches data quality issues early.

**What It Does:**

- Defines a Pandera schema with type checks and value constraints
- Validates `data/sample_employees.csv` against the schema
- Fails gracefully with clear error messages if validation fails

**Run:**

```bash
python src/validate_data_schema.py
```

**Best Practice:**  
Define schemas for all critical datasets. Run validation as the first step in any pipeline before processing data further. Treat schema violations as pipeline failures.

## Step 3: Version Your Datasets with DVC

**Script:** `src/version_data_with_dvc.sh`

**Why Third?**  
After validation passes, version your datasets. This ensures reproducibility—you can always go back to the exact data used for a specific model version.

**What It Does:**

- Initializes DVC in your Git repository
- Tracks `data/versioned_training_data.csv` with DVC
- Creates a `.dvc` file that Git tracks (while DVC handles the actual data)

**Run:**

```bash
bash src/version_data_with_dvc.sh
```

**Best Practice:**  
Version datasets alongside your code. When you train a model, you can track exactly which data version was used. Use DVC tags to mark important dataset versions (e.g., `dvc tag -a v1.0-training-set`).

## Step 4: Register in Data Catalog

**Script:** `src/register_data_catalog.py`

**Why Fourth?**  
After versioning, register your dataset in a metadata catalog. This creates discoverability—your team can find and understand datasets.

**What It Does:**

- Creates a unique ID for the dataset
- Logs metadata: name, description, storage path
- Appends to `data_catalog.jsonl` (a lightweight catalog)

**Run:**

```bash
python src/register_data_catalog.py
```

**Best Practice:**  
Register every production dataset. Include rich descriptions and tags. In larger organizations, use tools like DataHub, Amundsen, or AWS Glue Data Catalog instead of JSONL.

## Step 5: Log Data Lineage

**Script:** `src/log_data_lineage.py`

**Why Fifth?**  
As data flows through your pipeline, log its lineage. This tracks where data came from, when it was created, and what transformations were applied.

**What It Does:**

- Reads `data/sample_training_data.csv`
- Logs metadata: origin, timestamp, row count, columns
- Appends to `metadata_log.jsonl`

**Run:**

```bash
python src/log_data_lineage.py
```

**Best Practice:**  
Call `log_metadata()` at every major stage of your pipeline (e.g., after ingestion, after cleaning, after feature engineering). This creates an audit trail for debugging and compliance.

## Step 6: Monitor Data Freshness

**Script:** `src/check_data_freshness.py`

**Why Sixth?**  
In production, data can become stale. Monitor freshness to ensure your pipeline is consuming recent data.

**What It Does:**

- Checks the age of `data/sample_training_data.csv`
- Warns if data is older than 24 hours (configurable threshold)

**Run:**

```bash
python src/check_data_freshness.py
```

**Best Practice:**  
Run freshness checks as a pre-flight step before model training or batch inference. Set alerts when data exceeds age thresholds. Adjust `max_hours` based on your use case (real-time vs. batch).

## Step 7: Detect Feature Drift

**Script:** `src/detect_feature_drift.py`

**Why Last?**  
After your pipeline is running, continuously monitor for feature drift. Changes in data distributions can degrade model performance.

**What It Does:**

- Compares `data/sample_old_data.csv` (reference) with `data/sample_new_data.csv` (current)
- Uses Kolmogorov-Smirnov test to detect distribution changes
- Reports which features have drifted

**Run:**

```bash
python src/detect_feature_drift.py
```

**Best Practice:**  
Run drift detection periodically (daily/weekly) or before retraining models. If drift is detected, investigate whether retraining is needed or if data quality issues exist. Track drift over time to understand seasonal patterns.

## Full Workflow Example

Here's how you'd run all scripts in sequence for a complete data engineering workflow:

```bash
# 1. Prototype ETL on sample data
python src/prototype_etl_sampling.py

# 2. Validate schema
python src/validate_data_schema.py

# 3. Version the dataset
bash src/version_data_with_dvc.sh

# 4. Register in catalog
python src/register_data_catalog.py

# 5. Log lineage
python src/log_data_lineage.py

# 6. Check freshness
python src/check_data_freshness.py

# 7. Detect drift
python src/detect_feature_drift.py
```

## Key Principles

### Early Stage (Development)
1. **Prototype First** → Fail fast on small samples
2. **Validate Early** → Catch bad data before it propagates
3. **Version Everything** → Reproducibility is non-negotiable

### Mid Stage (Deployment)
4. **Catalog Assets** → Make data discoverable
5. **Track Lineage** → Know where data came from

### Late Stage (Production Monitoring)
6. **Monitor Freshness** → Detect pipeline failures
7. **Detect Drift** → Catch data quality degradation

## Dependencies

Ensure you have these installed:

```bash
uv add pandas pandera scipy dvc
# or
uv sync
```

## When to Run Each Script

| Script | Frequency | Context |
|--------|-----------|---------|
| `prototype_etl_sampling.py` | Once during development | When designing new ETL logic |
| `validate_data_schema.py` | Every pipeline run | Before processing any data |
| `version_data_with_dvc.sh` | On dataset changes | When data is updated |
| `register_data_catalog.py` | Once per new dataset | When creating a new data asset |
| `log_data_lineage.py` | Every transformation | At each pipeline stage |
| `check_data_freshness.py` | Before critical operations | Before training/inference |
| `detect_feature_drift.py` | Periodically (daily/weekly) | As part of model monitoring |

## Adapting for Production

These scripts are learning examples. For production, consider:

- **Orchestration:** Use Airflow, Prefect, or Dagster to schedule these checks
- **Monitoring:** Integrate with DataDog, Grafana, or CloudWatch for alerts
- **Storage:** Replace JSONL with proper databases (PostgreSQL, MongoDB)
- **Catalogs:** Use enterprise tools (DataHub, Amundsen, AWS Glue)
- **Lineage:** Consider Apache Atlas, OpenLineage, or Marquez
- **Testing:** Add unit tests for each function with pytest

## Summary

Good data engineering is about building habits:

1. **Prototype fast** → iterate quickly
2. **Validate always** → trust your data
3. **Version everything** → enable reproducibility
4. **Document thoroughly** → make data discoverable
5. **Track lineage** → understand data flow
6. **Monitor continuously** → catch issues early
7. **Detect drift** → maintain quality over time

This follows the principle of "shift left" in data engineering—catching issues as early as possible in the workflow to prevent costly failures downstream.

Follow this workflow, and your ML pipeline will thank you at 3 AM.

<br>
