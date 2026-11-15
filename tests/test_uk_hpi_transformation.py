import pandas as pd

from housing.transformation.uk_hpi import transform_uk_hpi_indices


def test_transform_uk_hpi_indices():
    raw_df = pd.DataFrame(
        {
            "Time period": ["Jan 2011", "Jul 2026 [r]", "Aug 2026 [p]"],
            "United Kingdom": [59.1, 104.3, 104.6],
            "Northern Ireland [note 3] ": [69.3, 124.6, 124.6],

        }
    )

    result = transform_uk_hpi_indices(raw_df)

    assert len(result) == 6
    assert list(result.columns) == [
        "reference_date",
        "area_name",
        "price_index",
        "observation_status",
    ]

    assert result.iloc[0]["reference_date"] == pd.Timestamp("2011-01-01")
    assert result.iloc[0]["area_name"] == "United Kingdom"
    assert result.iloc[0]["price_index"] == 59.1