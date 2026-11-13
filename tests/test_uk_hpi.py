from pathlib import Path

import pandas as pd 

from housing.ingestion.uk_hpi import extract_uk_hpi_indices

def test_extract_uk_hpi_indices():
    source_path = Path("data/uk_house_price_index.xlsx")

    df = extract_uk_hpi_indices(source_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (188,16)
    assert "Time period" in df.columns
    assert "England" in df.columns
    assert "United Kingdom" in df.columns