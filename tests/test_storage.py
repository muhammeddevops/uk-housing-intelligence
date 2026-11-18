from pathlib import Path

from housing.storage.local import store_bronze_file

def test_store_bronze_file(tmp_path):
    source_path = tmp_path / "source.xlsx"
    destination_path = tmp_path / "bronze" / "uk_hpi" / "source.xlsx"

    source_path.write_bytes(b"test file content")

    result = store_bronze_file(source_path, destination_path)

    assert result == destination_path
    assert destination_path.exists()
    assert destination_path.read_bytes() == b"test file content"