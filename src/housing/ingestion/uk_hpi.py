from pathlib import Path

import pandas as pd

UK_HPI_INDEX_SHEET = "1"
UK_HPI_HEADER_ROW = 2

def extract_uk_hpi_indices(source_path: Path) -> pd.DataFrame:
    """Extract UK HPI index data from the source workbook."""
    return pd.read_excel(
        source_path,
        sheet_name=UK_HPI_INDEX_SHEET,
        header=UK_HPI_HEADER_ROW       
    )
