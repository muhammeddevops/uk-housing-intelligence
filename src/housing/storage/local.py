import shutil
from pathlib import Path

def store_bronze_file(source_path: Path, destination_path: Path) -> Path:
    """"Copy an original source file into the Bronze layer"""

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source_path, destination_path)

    return destination_path
