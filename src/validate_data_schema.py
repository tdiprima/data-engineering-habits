# This script defines a schema using Pandera to validate a DataFrame's structure,
# types, and value constraints (e.g., age range, valid countries). It reads
# from a CSV, validates it, and handles validation errors gracefully.

from pathlib import Path

import pandas as pd
from pandera import Check, Column, DataFrameSchema
from pandera.errors import SchemaError

schema = DataFrameSchema(
    {
        "age": Column(int, Check.in_range(0, 120)),
        "salary": Column(float, Check.greater_than_or_equal_to(0)),
        "country": Column(str, Check.isin(["US", "UK", "IN", "CA", "DE"])),
    }
)

try:
    df = pd.read_csv("../data/sample_employees.csv")
    validated_df = schema.validate(df)
    print("Data validated successfully.")
except SchemaError as e:
    print(f"Validation failed: {e}")
