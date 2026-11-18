from pathlib import Path

from housing.config import BRONZE_DATA_DIR, SILVER_DATA_DIR
from housing.ingestion.uk_hpi import extract_uk_hpi_indices
from housing.storage.local import store_bronze_file, store_silver_parquet
from housing.transformation.uk_hpi import transform_uk_hpi_indices

def run_uk_hpi_pipeline(source_path: Path) -> Path:
    """Run the UK HPI ingestion and transformation pipeline."""

    bronze_path = BRONZE_DATA_DIR / "uk_hpi" / source_path.name
    silver_path = SILVER_DATA_DIR / "uk_hpi" / "uk_hpi_indices.parquet"

    store_bronze_file(source_path, bronze_path)

    raw_df = extract_uk_hpi_indices(bronze_path)

    transformed_df = transform_uk_hpi_indices(raw_df)

    return store_silver_parquet(transformed_df, silver_path)