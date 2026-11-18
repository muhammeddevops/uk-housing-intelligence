from pathlib import Path
import pandas as pd

from housing.storage.local import store_bronze_file, store_silver_parquet

def test_store_bronze_file(tmp_path):
    source_path = tmp_path / "source.xlsx"
    destination_path = tmp_path / "bronze" / "uk_hpi" / "source.xlsx"

    source_path.write_bytes(b"test file content")

    result = store_bronze_file(source_path, destination_path)

    assert result == destination_path
    assert destination_path.exists()
    assert destination_path.read_bytes() == b"test file content"


def test_store_silver_parquet(tmp_path):
    destination_path = tmp_path / "silver" / "uk_hpi" / "uk_hpi.parquet"

    df = pd.DataFrame(
        {
            "area_name" : ["England", "Wales"],
            "price_index": [125.4, 118.2],
        }
    )

    result = store_silver_parquet(df, destination_path)

    stored_df = pd.read_parquet(destination_path)

    assert result == destination_path
    assert destination_path.exists()
    pd.testing.assert_frame_equal(stored_df, df)