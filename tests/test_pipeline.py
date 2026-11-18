import pandas as pd

from housing.pipeline import run_uk_hpi_pipeline

def test_run_uk_hpi_pipeline(tmp_path, monkeypatch):
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

    bronze_dir = tmp_path / "bronze"
    silver_dir = tmp_path / "silver"

    monkeypatch.setattr(
        "housing.pipeline.BRONZE_DATA_DIR",
        bronze_dir
    )
    monkeypatch.setattr(
        "housing.pipeline.SILVER_DATA_DIR",
        silver_dir,
    )

    result = run_uk_hpi_pipeline(source_path)

    bronze_path = bronze_dir / "uk_hpi" / source_path.name
    silver_path = silver_dir / "uk_hpi" / "uk_hpi_indices.parquet"

    assert result == silver_path
    assert bronze_path.exists()
    assert silver_path.exists()

    stored_df = pd.read_parquet(silver_path)

    assert len(stored_df) == 4
    assert list(stored_df.columns) == [
        "reference_date",
        "area_name",
        "price_index",
        "observation_status",
    ]

    assert stored_df["area_name"].nunique() == 2
    assert not stored_df.isna().any().any()
    