import shutil
from pathlib import Path

import pandas as pd

def store_bronze_file(source_path: Path, destination_path: Path) -> Path:
    """Copy an original source file into the Bronze layer"""

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source_path, destination_path)

    return destination_path


def store_silver_parquet(df: pd.DataFrame, destination_path: Path) -> Path:
    """Store transformed data as a Parquet file in the silver layer."""

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(destination_path, index=False)

    return destination_path

