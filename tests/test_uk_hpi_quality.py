from pathlib import Path

from housing.ingestion.uk_hpi import extract_uk_hpi_indices
from housing.transformation.uk_hpi import transform_uk_hpi_indices

def test_transform_uk_hpi_indices_data_quality():
    raw_df = extract_uk_hpi_indices(Path("data/uk_house_price_index.xlsx"))
    df = transform_uk_hpi_indices(raw_df)

    assert not  df.isna().any().any()
    assert not df.duplicated(
        subset=["reference_date", "area_name"]
    ).any()
    assert df["reference_date"].notna().all()
    assert df["area_name"].nunique() == 15
    assert (df["price_index"] > 0).all