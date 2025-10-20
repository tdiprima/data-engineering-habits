#!/bin/bash
# This shell script initializes DVC in a Git repo, adds a csv file to DVC for
# versioning, and commits the changes to Git for reproducible dataset tracking.

# Initialize DVC and track the dataset
dvc init
dvc add ../data/versioned_training_data.csv
git add ../data/versioned_training_data.csv.dvc .gitignore
git commit -m "Track initial dataset version with DVC"
echo "Dataset versioned successfully."
