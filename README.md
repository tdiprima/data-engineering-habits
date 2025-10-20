# 🧠 ML Data Engineering Habits (but make it ✨clean✨)

![Personal Repo](https://img.shields.io/badge/🔒-personal_repo-blueviolet?style=for-the-badge)

Welcome to the **data engineer's survival kit** — a collection of Python + shell scripts showing how to actually keep your ML data projects from turning into chaos.  
We're talkin' **validation**, **versioning**, **lineage**, and **vibes** (the observability kind).

## 🗂️ What's Inside

* `log_data_lineage.py` → Keeps receipts (logs your DataFrame metadata for traceability).
* `validate_data_schema.py` → Checks your data before it embarrasses you in prod.
* `version_data_with_dvc.sh` → Handles dataset versioning with DVC like a boss.
* `detect_feature_drift.py` → Calls out data drift before it ruins your model's day.
* `prototype_etl_sampling.py` → Makes sampling huge datasets actually chill for prototyping.
* `register_data_catalog.py` → Gets your datasets living rent-free in a metadata catalog.
* `check_data_freshness.py` → Tells you if your data's getting crusty (freshness checks 🔍).

## ⚙️ How to Use

Run each script solo using Python (or bash if it's the `.sh` one).  
You'll need **Git** + **DVC** for the versioning magic.

```sh
python validate_data_schema.py
bash version_data_with_dvc.sh
```

## 🚀 Setup (fr, it's easy)

Use **uv** to install what you need:

```sh
uv add pandas pandera scipy dvc
# or:
uv sync
```

## 💡 TL;DR

These scripts = good data habits.  
Good data habits = happy ML pipeline.  
Happy ML pipeline = less 3AM debugging. 🧘‍♂️
