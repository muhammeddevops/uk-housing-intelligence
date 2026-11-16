
import pandas as pd


def transform_uk_hpi_indices(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Transform UK HPI index data from wide to long format."""

    df = raw_df.copy()

    # Extract the reference period and revision marker.
    period_parts = df["Time period"].str.extract(
        r"^(?P<period>.+?)(?:\s*\[(?P<marker>[pr])\])?$"
    )

    # Convert the period into a datetime value.
    df["reference_date"] = pd.to_datetime(
        period_parts["period"],
        format="mixed",
    )

    # Convert revision markers into descriptive statuses.
    df["observation_status"] = (
        period_parts["marker"]
        .map({"p": "provisional", "r": "revised"})
        .fillna("unmarked")
    )

    # Remove the original time period column.
    df = df.drop(columns=["Time period"])

     # Clean geographical column names.
    df.columns = (
        df.columns
        .str.replace(r"\s*\[note \d+\]", "", regex=True)
        .str.strip()
    )

    # Reshape geographical columns into individual rows.
    df = df.melt(
        id_vars=["reference_date", "observation_status"],
        var_name="area_name",
        value_name="price_index",
    )


    return df[
        ["reference_date", "area_name", "price_index", "observation_status"]
    ]
