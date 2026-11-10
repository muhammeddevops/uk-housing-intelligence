# Data Sources

## 1. UK House Price Index (UK HPI)

### Overview

The UK House Price Index (UK HPI) measures changes in residential property prices across the United Kingdom.

It is produced using property transaction data from HM Land Registry, Registers of Scotland and Land and Property Services Northern Ireland.

The dataset provides information on average house prices, price indices and percentage changes over time. It also includes breakdowns by property type, buyer status and geographical area.

### Source Information

| Attribute             | Details                                                                |
| --------------------- | ---------------------------------------------------------------------- |
| Source                | UK House Price Index                                                   |
| Provider              | HM Land Registry / Office for National Statistics                      |
| Official website      | https://www.gov.uk/government/collections/uk-house-price-index-reports |
| Download format       | Excel (.xlsx)                                                          |
| Update frequency      | Monthly (Northern Ireland figures are quarterly)                       |
| Geographical coverage | United Kingdom                                                         |
| Historical coverage   | Varies by geography and measure                                        |
| Licence               | Open Government Licence v3.0                                           |

### Data Structure

The October 2026 workbook contains 13 worksheets, including:

- House price indices
- Average house prices
- Annual percentage changes
- First-time buyers and former owner-occupiers
- New-build and pre-owned properties
- Cash and mortgage buyers
- Local authority house prices

The workbook includes national, regional and local authority breakdowns.

### Key Fields

| Field         | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| Date          | Reference period for the house price observation                     |
| AreaCode      | Official geographical identifier                                     |
| AreaName      | Name of the geographical area                                        |
| AveragePrice  | Average residential property price in GBP                            |
| Index         | House price index value                                              |
| AnnualChange  | Percentage change compared with the same period in the previous year |
| MonthlyChange | Percentage change compared with the previous month                   |

_Note: Actual column names and data types will be confirmed during ingestion and transformation._

### Known Limitations

- Northern Ireland local authority figures are reported quarterly, unlike the monthly figures for England, Wales and Scotland.
- Recent observations may be provisional and subject to revision.
- Some supplementary measures have different geographical coverage from the headline UK HPI.
- Local authority worksheets in the downloaded workbook contain the latest available period rather than a complete historical series.
- The first-time buyer and former owner-occupier supplementary series have a weighting issue affecting comparisons before and after January 2026.

### Planned Ingestion Approach

The initial dataset will be downloaded as an Excel workbook and retained in its original format within the project's raw data storage.

The ingestion pipeline will:

1. Retrieve the latest available workbook.
2. Validate the downloaded file.
3. Extract relevant worksheets.
4. Standardise column names and data types.
5. Convert reporting periods into consistent date fields.
6. Preserve geographical identifiers and observation status.
7. Load the extracted data into the appropriate storage layer.

The ingestion process will be designed to support repeatable and incremental updates.

## 2. Price Index of Private Rents (PIPR)

### Overview

The Price Index of Private Rents (PIPR) is published by the Office for National Statistics (ONS). It measures changes in private rental prices across the UK, covering both new and existing tenancies.

The dataset provides rental price indices, average rental prices and monthly and annual percentage changes. It also includes breakdowns by bedroom count and property type.

### Source Information

| Attribute             | Details                                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Source                | Price Index of Private Rents (PIPR)                                                                               |
| Provider              | Office for National Statistics                                                                                    |
| Official website      | https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/priceindexofprivaterentsukmonthlypricestatistics |
| Download format       | Excel (.xlsx)                                                                                                     |
| Update frequency      | Monthly                                                                                                           |
| Historical coverage   | January 2015 onwards                                                                                              |
| Geographical coverage | UK, countries, regions and local areas                                                                            |
| Licence               | Open Government Licence v3.0                                                                                      |
| Publication examined  | 21 October 2026                                                                                                   |

### Data Structure

The downloaded workbook contains four worksheets, with the main statistics stored in `Table 1`.

The main table contains:

- 50,337 observations.
- 40 columns.
- 357 geographical areas or area groupings.
- 141 monthly reporting periods, from January 2015 to September 2026.

The dataset provides nine rental property categories, including overall rental prices, bedroom counts and property types.

Each category contains an index, monthly percentage change, annual percentage change and rental price.

### Key Fields

| Field                  | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| Time period            | Month the observation relates to                                    |
| Area code              | Geographical identifier, where applicable                           |
| Area name              | Name of the geographical area                                       |
| Region or country name | Associated region or country                                        |
| Index                  | Rental price index, with January 2023 = 100                         |
| Monthly change         | Percentage change compared with the previous month                  |
| Annual change          | Percentage change compared with the same month in the previous year |
| Rental price           | Average private rental price in GBP                                 |

Additional columns provide equivalent measures for bedroom counts and property types.

### Known Limitations

- The published PIPR series begins in January 2015.
- Northern Ireland rental data is unavailable for the latest two months. UK aggregate figures for these months use estimates based on previous Northern Ireland rental inflation rates.
- `[x]` represents unavailable data, while `[z]` represents data that is not applicable.
- The data is not seasonally adjusted.
- The index uses January 2023 as its base period, equal to 100.
- Scotland rental statistics are mainly based on advertised new lets, which affects comparisons with other UK countries.
- The ONS advises caution when comparing the current series with the earlier historical series because of a methodology change in January 2015.
- The statistics are classified as official statistics in development.

### Planned Ingestion Approach

The original Excel workbook will be retained in raw storage.

The ingestion pipeline will:

1. Retrieve and validate the latest workbook.
2. Extract the main statistics from `Table 1`.
3. Standardise column names and data types.
4. Convert reporting periods into date fields.
5. Preserve geographical identifiers.
6. Handle `[x]` and `[z]` markers explicitly.
7. Separate rental measures into a consistent analytical structure.
8. Load the processed data into the appropriate storage layer.

The pipeline must preserve the distinction between unavailable data, non-applicable data and valid numerical observations.
