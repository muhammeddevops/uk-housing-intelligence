import pandas as pd

from housing.ingestion.uk_hpi import extract_uk_hpi_indices


def test_extract_uk_hpi_indices(tmp_path):
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
    
    df = extract_uk_hpi_indices(source_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2,3)
    assert "Time period" in df.columns
    assert "England" in df.columns
    assert "United Kingdom" in df.columns