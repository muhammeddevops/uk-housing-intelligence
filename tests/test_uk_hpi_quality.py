import pandas as pd

from housing.ingestion.uk_hpi import extract_uk_hpi_indices
from housing.transformation.uk_hpi import transform_uk_hpi_indices

def test_transform_uk_hpi_indices_data_quality(tmp_path):

    source_path = tmp_path / "uk_house_price_index.xlsx"

    source_df = pd.DataFrame(
        {
            "Time period": ["Jan 2025", "Feb 2025"],
            "United Kingdom": [100.1, 100.5],
            "England": [101.2, 101.6],
        }
    )

    source_df.to_excel(
        source_path,
        sheet_name="1",
        index=False,
        startrow=2,
    )

    raw_df = extract_uk_hpi_indices(source_path)
    df = transform_uk_hpi_indices(raw_df)

    assert not  df.isna().any().any()
    assert not df.duplicated(
        subset=["reference_date", "area_name"]
    ).any()
    assert df["area_name"].nunique() == 2
    assert (df["price_index"] > 0).all