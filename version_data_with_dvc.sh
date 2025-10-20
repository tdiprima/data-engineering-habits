#!/bin/bash
# This shell script initializes DVC in a Git repo, generates a sample CSV, 
# adds it to DVC for versioning, and commits the changes to Git for reproducible dataset tracking.

# Generate a sample CSV if needed
echo "id,name,age" > versioned_training_data.csv
echo "1,Alice,30" >> versioned_training_data.csv
echo "2,Bob,45" >> versioned_training_data.csv
echo "3,Charlie,25" >> versioned_training_data.csv

# Initialize DVC and track the dataset
dvc init
dvc add versioned_training_data.csv
git add versioned_training_data.csv.dvc .gitignore
git commit -m "Track initial dataset version with DVC"
echo "Dataset versioned successfully."
