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
