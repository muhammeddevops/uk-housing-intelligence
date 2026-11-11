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

---

## 3. Annual Survey of Hours and Earnings (ASHE) – Table 8

### Overview

The Annual Survey of Hours and Earnings (ASHE) is the ONS's main source of information on employee earnings in the UK. It is based on a 1% sample of employee jobs taken from HM Revenue and Customs PAYE records.

Table 8 presents earnings by **place of residence**, meaning where employees live rather than where they work. This is the right basis for housing affordability, because housing costs are paid where people live.

Four workbooks from the Table 8 release are used:

| Table | Content                            | Purpose                                     |
| ----- | ---------------------------------- | ------------------------------------------- |
| 8.1a  | Weekly pay – gross (£)             | Earnings for rent-to-earnings comparisons   |
| 8.1b  | Coefficients of variation for 8.1a | Statistical reliability of weekly pay       |
| 8.7a  | Annual pay – gross (£)             | Earnings for house-price-to-earnings ratios |
| 8.7b  | Coefficients of variation for 8.7a | Statistical reliability of annual pay       |

The selected measure is **median gross earnings for full-time employees**:

- The median is less affected by very high earners than the mean.
- Gross pay is measured before tax.
- Full-time employees give a more consistent comparison between areas.

### Source Information

| Attribute             | Details                                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Source                | ASHE Table 8 – Place of residence by local authority                                                                                      |
| Provider              | Office for National Statistics                                                                                                            |
| Official website      | https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/placeofresidencebylocalauthorityashetable8 |
| Download format       | ZIP archive containing 22 Excel (.xlsx) workbooks                                                                                         |
| Update frequency      | Annual (provisional each autumn, revised the following year)                                                                              |
| Reference period      | April of the survey year                                                                                                                  |
| Historical coverage   | One year per edition. Earlier years require earlier editions                                                                              |
| Geographical coverage | UK, countries, regions, counties and local authorities (no Northern Ireland local authorities)                                            |
| Licence               | Open Government Licence v3.0                                                                                                              |
| Publication examined  | 2026 provisional, released 22 October 2026                                                                                                |
| Local files           | `data/ashe_table_8_2026/PROV - Home Geography Table 8.{1a,1b,7a,7b} ... 2026[ CV].xlsx`                                                   |

### Data Structure

All four workbooks share the same layout:

- 10 worksheets: a notes sheet plus 9 data sheets (All, Male, Female, Full-Time, Part-Time, Male Full-Time, Male Part-Time, Female Full-Time, Female Part-Time).
- The **Full-Time** sheet is used.
- Rows 1–5 are headers (title, blank row, three stacked header rows). Data starts at row 6.
- 395 coded geography rows per sheet, plus one uncoded "Not Classified" row and footnotes.
- The same 395 area codes appear in all four workbooks, so one parser can handle every table.

Geographical levels (Full-Time sheet):

| Code prefix        | Level                           | Rows   |
| ------------------ | ------------------------------- | ------ |
| K02 / K03 / K04    | UK / GB / England and Wales     | 1 each |
| E92, W92, S92, N92 | Countries                       | 1 each |
| E12                | English regions                 | 9      |
| E13                | Inner / Outer London            | 2      |
| E11                | Metropolitan counties           | 6      |
| E10                | Shire counties                  | 21     |
| E06                | Unitary authorities             | 63     |
| E07                | Shire districts                 | 164    |
| E08                | Metropolitan districts          | 36     |
| E09                | London boroughs                 | 33     |
| W06                | Welsh unitary authorities       | 22     |
| S12                | Scottish council areas          | 32     |
| N92                | Northern Ireland (country only) | 1      |

Lower-tier local authorities (E06, E07, E08, E09, W06, S12) total 350.

### Key Fields

| Col | Source header                                      | Proposed field                                        |
| --- | -------------------------------------------------- | ----------------------------------------------------- |
| A   | Description                                        | `area_name`                                           |
| B   | Code                                               | `area_code`                                           |
| C   | Number of jobs (thousand)                          | `job_count_thousands` (indicative only)               |
| D   | Median                                             | `median_pay_gbp`                                      |
| E   | Annual percentage change (median)                  | `median_annual_change_pct`                            |
| F   | Mean                                               | `mean_pay_gbp`                                        |
| G   | Annual percentage change (mean)                    | `mean_annual_change_pct`                              |
| H–Q | Percentiles 10, 20, 25, 30, 40, 60, 70, 75, 80, 90 | `p10` … `p90` (or long format: `percentile`, `value`) |

In the CV workbooks (8.1b, 8.7b), the same columns hold coefficients of variation (%) instead of pay values. They become `*_cv_pct` fields joined on `area_code`.

Pay values are weekly (£) in 8.1a and annual (£) in 8.7a. A `pay_period` attribute (`weekly` / `annual`) distinguishes them.

### Known Limitations

- **No Northern Ireland local authority data.** Only the NI country total is published. NI council-level earnings come from NISRA (Section 5).
- **Weekly and annual pay cover different populations.** Annual pay (8.7a) covers employees in the same job for more than a year. Weekly pay (8.1a) covers employees whose pay was not affected by absence. Full-time UK job counts: 18,184k (annual) vs 20,653k (weekly).
- **Annual pay is not weekly pay × 52.** Across local authorities, annual median ÷ weekly median ranges from 46.2 to 55.1 (mean 50.5). Multiplying weekly by 52 would overstate annual earnings by about 3% on average.
- **Annual medians are less precise than weekly medians.** Lower-tier local authority median CV bands:

| CV band                    | Annual (8.7b) | Weekly (8.1b) |
| -------------------------- | ------------- | ------------- |
| ≤5% (precise)              | 86            | 186           |
| 5–10% (reasonably precise) | 226           | 159           |
| 10–20% (acceptable)        | 34            | 4             |
| >20% (suppressed)          | 4             | 1             |

Least precise annual medians: South Staffordshire and Hertsmere (17%), Chichester (15%), Westminster, West Devon, Surrey Heath, Rutland, Redcar and Cleveland, Maldon (14%).

- **Suppressed medians.** No annual median for City of London (E09000001), Isles of Scilly (E06000053), Monmouthshire (W06000021) or Orkney Islands (S12000023). Isles of Scilly also has no weekly median.
- **Provisional estimates.** Each edition is provisional and is revised in the following year's release.
- **Number of jobs** is described by ONS as indicative only and must not be used as a weight or denominator.
- **Quality bands are encoded as cell fill colours** in 8.1a and 8.7a, which pandas does not read. Numeric CVs come from 8.1b and 8.7b instead. The CV bands were checked and match the fill colours exactly.

### Data Quality Rules

| Issue                                          | Handling                                                                         |
| ---------------------------------------------- | -------------------------------------------------------------------------------- |
| Codes have a leading apostrophe (`'E06000005`) | Strip during ingestion                                                           |
| Names have trailing spaces (247 of 395 rows)   | Trim during ingestion                                                            |
| Hierarchy shown by leading spaces in names     | Do not rely on it. Derive levels from code prefixes                              |
| Counties and their districts both present      | Filter to lower-tier codes for local authority analysis to avoid double counting |
| `x` (CV > 20%, unreliable)                     | Load as null with `suppression_reason = 'unreliable'`                            |
| `..` (disclosive)                              | Load as null with `suppression_reason = 'disclosive'`                            |
| `.` in CV workbooks (annual change columns)    | Not applicable. CVs are not calculated for percentage changes                    |
| "Not Classified" row                           | Exclude                                                                          |
| Footnote rows                                  | Exclude (no valid area code)                                                     |

### Planned Ingestion Approach

The original ZIP archive and extracted workbooks will be retained in raw storage.

The ingestion pipeline will:

1. Retrieve and validate the four required workbooks (8.1a, 8.1b, 8.7a, 8.7b).
2. Read the Full-Time sheet from each, starting at row 6.
3. Keep only rows with a valid area code, and strip the apostrophe prefix.
4. Trim area names and derive the geography level from the code prefix.
5. Convert `x` and `..` to nulls, recording the suppression reason.
6. Join each pay table to its CV table on `area_code`, and assign a `quality_band`.
7. Add `reference_date` (April of the survey year), `pay_period`, `edition` (`provisional` / `revised`), `published_at` and `ingested_at`.
8. Load the processed data into the appropriate storage layer.

### Modelling Implications

- **Grain** (proposed `fact_earnings`): one row per `area_code` × `reference_year` × `worker_group` × `pay_period` × `edition`.
- **Revisions:** revised values supersede provisional ones in the marts, but both are kept in storage.
- **History:** ingest earlier editions, preferably the revised version of each year, to build a time series.
- **Affordability ratios:** use the 8.7a annual median for house-price-to-earnings and the 8.1a weekly median for rent-to-earnings. Do not convert between them.
- **Rankings:** single-year local authority rankings can be driven by sampling noise. Carry `median_cv_pct` and `quality_band` through to the marts and show them in Power BI. Add a dbt warning for ratios built on earnings with CV > 10%, and consider a rolling 3-year median for rankings.
- **Geography harmonisation:** ASHE has 296 England lower-tier local authorities, while UK HPI has 295. The difference is Isles of Scilly (E06000053), which is absent from UK HPI (see Section 1).

## 4. ONS Mid-Year Population Estimates

### Overview

The mid-year population estimates (MYE) are the official estimates of the usually resident population of the UK on 30 June each year. They are published by ONS and combine estimates from ONS (England and Wales), National Records of Scotland and NISRA (Northern Ireland).

The detailed time-series workbook provides population by local authority, sex and single year of age, plus the components of population change (births, deaths, internal and international migration).

Population is used as context for affordability. Examples: population growth versus house price growth, and per-capita measures.

### Source Information

| Attribute             | Details                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source                | Population estimates: detailed time series 2011 to 2025, UK, local authorities, sex and age                                                                               |
| Provider              | Office for National Statistics (with NRS and NISRA)                                                                                                                       |
| Official website      | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland |
| Download format       | Excel (.xlsx)                                                                                                                                                             |
| Release number        | MYE25UK                                                                                                                                                                   |
| Update frequency      | Annual (next release summer 2027)                                                                                                                                         |
| Reference date        | 30 June of each year                                                                                                                                                      |
| Historical coverage   | Mid-2011 to mid-2025                                                                                                                                                      |
| Geographical coverage | UK, constituent countries and all 361 local authorities, Northern Ireland included                                                                                        |
| Geography version     | Local authority boundaries as of April 2023 (`ladcode23`)                                                                                                                 |
| Licence               | Open Government Licence v3.0                                                                                                                                              |
| Publication examined  | 1 October 2026                                                                                                                                                            |
| Local file            | `data/myebtablesuk20112025.xlsx`                                                                                                                                          |

### Data Structure

The workbook contains a cover sheet, contents, notes, related publications and five data tables:

| Sheet | Content                                                           | Geography                          | Rows   |
| ----- | ----------------------------------------------------------------- | ---------------------------------- | ------ |
| MYEB1 | Population by local authority, sex and single year of age (0–90+) | UK local authorities (361)         | 65,702 |
| MYEB2 | MYEB1 plus components of change by age and sex                    | England and Wales only (318)       | 57,876 |
| MYEB3 | Total population and components of change by local authority      | UK local authorities (361)         | 361    |
| MYEB4 | Population by country, sex and single year of age                 | UK, GB, E&W and the four countries | 1,274  |
| MYEB5 | Total population and components of change by country              | UK, GB, E&W and the four countries | 7      |

**MYEB3 is the main table**, because it gives one row per local authority with total population for every year, so ages don't need summing. MYEB1 is kept for later age-based analysis (e.g. working-age population).

Unlike ASHE, the tables are clean: a single header row (row 2), data from row 3, plain area codes (no apostrophes) and no suppression markers in the local authority tables.

Local authority coverage (MYEB3):

| Code prefix | Level                                       | Rows |
| ----------- | ------------------------------------------- | ---- |
| E06         | Unitary authorities                         | 63   |
| E07         | Shire districts                             | 164  |
| E08         | Metropolitan districts                      | 36   |
| E09         | London boroughs                             | 33   |
| W06         | Welsh unitary authorities                   | 22   |
| S12         | Scottish council areas                      | 32   |
| N09         | Northern Ireland local government districts | 11   |

Only lower-tier local authorities are present (no counties or regions), so there is no double-counting risk.

### Key Fields

MYEB3 (wide format, one block of columns per year):

| Source column                   | Description                               | Proposed field                                               |
| ------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| `ladcode23`                     | Local authority code (2023 boundaries)    | `area_code`                                                  |
| `laname23`                      | Local authority name                      | `area_name`                                                  |
| `country`                       | E, W, S or N                              | `country_code`                                               |
| `population_YYYY`               | Mid-year population estimate              | `population`                                                 |
| `births_YYYY`, `deaths_YYYY`    | Births and deaths in the year to mid-YYYY | `births`, `deaths`                                           |
| `natchange_YYYY`                | Natural change (births − deaths)          | `natural_change`                                             |
| `internal_in/out/net_YYYY`      | Moves between UK local authorities        | `internal_in`, `internal_out`, `internal_net`                |
| `international_in/out/net_YYYY` | International migration                   | `international_in`, `international_out`, `international_net` |
| `other_change_YYYY`             | Other adjustments                         | `other_change`                                               |

MYEB1 adds `sex` (Female / Male) and `age` (0–90, where 90 = 90 and over).

### Known Limitations

- **Earlier years are revised in each release.** Mid-2022 to mid-2024 were revised in October 2026 (England, Wales and Scotland; Northern Ireland not revised). ONS advises using the full time series from the latest release rather than appending new years to older releases.
- **Geography uses 2023 boundaries, which differ from ASHE 2026.** ASHE uses Barnsley `E08000038` and Sheffield `E08000039`, but population uses the older codes `E08000016` and `E08000019`. This was the only mismatch among England, Wales and Scotland local authorities.
- **Country totals are not the sum of local authority figures** (MYEB5 vs MYEB3), mainly because of rounding in Scotland and Northern Ireland.
- **Different methods per country.** England and Wales, Scotland and Northern Ireland are produced by different agencies with different methods.
- **Unrounded but not precise.** Estimates are published unrounded, but ONS states they should not be taken as accurate to that level of detail. Uncertainty is higher for smaller areas.
- **MYEB2 covers England and Wales only.**
- **"NO DATA"** appears in MYEB5 for UK and GB internal migration, where internal moves cancel out at national level.

### Data Quality Rules

| Issue                                         | Handling                                                                                           |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Wide format (one column per year and measure) | Unpivot to long format: `area_code`, `reference_year`, `measure`, `value`                          |
| Revised history                               | Full reload of the whole series on each release, versioned by `published_at`                       |
| 2023 vs later geography codes                 | Map through `dim_geography` (code-change table), not by joining codes directly                     |
| Country totals ≠ sum of local authorities     | Use MYEB5 for country totals. Don't aggregate MYEB3 upwards                                        |
| `NO DATA` in MYEB5                            | Load as null with a reason, not as zero                                                            |
| Age 90 means 90+                              | Store as an age band (`90+`), not as a single age                                                  |
| Row counts                                    | Validate against the counts stated in the Notes sheet (e.g. MYEB1 = 65,702 rows, MYEB3 = 361 rows) |

### Planned Ingestion Approach

The original workbook will be retained in raw storage.

The ingestion pipeline will:

1. Retrieve and validate the latest workbook.
2. Extract MYEB3 (and MYEB1 for age analysis) using row 2 as the header.
3. Validate row counts against the Notes sheet.
4. Unpivot year columns into long format.
5. Add `reference_date` (30 June of each year), `geography_version` (`2023`), `published_at` and `ingested_at`.
6. Replace the previous series in full, keeping earlier versions in storage for audit.
7. Load the processed data into the appropriate storage layer.

### Modelling Implications

- **Grain** (proposed `fact_population`): one row per `area_code` × `reference_year` × `published_at`. Components of change can be columns or a separate `fact_population_change`.
- **Load strategy:** full refresh each release. This is deliberately different from Price Paid Data (incremental). The load strategy depends on whether a source revises its history.
- **Geography:** the Barnsley / Sheffield code change is the first concrete case for a `dim_geography` mapping table with effective dates, joining 2023 codes to 2024+ codes.
- **Northern Ireland:** this is the first source in the project with complete NI local authority coverage (N09 codes). It can become the reference list of 361 local authorities that other sources are checked against.

## 5. NISRA ASHE – Northern Ireland Local Government Districts

### Overview

ONS ASHE Table 8 (Section 3) has no Northern Ireland local authority breakdown. NISRA publishes the equivalent Table 8 for Northern Ireland's 11 Local Government Districts (LGDs), from the same survey and on the same definitions. Together the two sources give earnings for all 361 UK local authorities.

As with Section 3, the **place of residence** tables are used.

### Source Information

| Attribute             | Details                                                                             |
| --------------------- | ----------------------------------------------------------------------------------- |
| Source                | ASHE 2026 (provisional) by Local Government District, by place of residence         |
| Provider              | Northern Ireland Statistics and Research Agency (NISRA)                             |
| Official website      | https://www.nisra.gov.uk/publications/ni-geographies-place-work-and-place-residence |
| Download              | https://www.nisra.gov.uk/files/nisra/documents/2026-10/ASHE-2026-home-lgd.zip       |
| Download format       | ZIP archive containing 11 Excel (.xlsx) workbooks                                   |
| Update frequency      | Annual (provisional each October, revised the following year)                       |
| Reference period      | April of the survey year (annual pay: tax year ending 5 April)                      |
| Historical coverage   | One year per edition. Editions available back to 2011 on the same page              |
| Geographical coverage | Northern Ireland total + 11 LGDs (N09 codes)                                        |
| Licence               | Open Government Licence v3.0                                                        |
| Publication examined  | 2026 provisional, published 22 October 2026 (same day as ONS)                       |
| Local files           | `data/nisra_ashe_2026_home_lgd/Home LGD14 Table 8 (NI).{1,7} ... 2026.xlsx`         |

Historical ZIP file names are inconsistent (e.g. `ASHE-Table-2023-3-revised.zip`, `2015_0.zip`), so URLs cannot be generated from a pattern. They should be listed in a config file.

### Data Structure

The ZIP contains 11 workbooks, one per measure (Table 8 (NI).1 to .11). Two are used:

| Workbook                          | Equivalent ONS table | Purpose                 |
| --------------------------------- | -------------------- | ----------------------- |
| Table 8 (NI).1 Weekly pay – Gross | 8.1a + 8.1b          | Rent-to-earnings        |
| Table 8 (NI).7 Annual pay – Gross | 8.7a + 8.7b          | House-price-to-earnings |

**Differences from the ONS layout:**

| Aspect              | ONS Table 8                     | NISRA Table 8 (NI)                                                                                             |
| ------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| CVs                 | Separate workbook (8.1b, 8.7b)  | Separate sheet in the same workbook (`Table8.1b Full-Time CV`)                                                 |
| Sheets              | 10 (`Full-Time`, …)             | 21: cover, contents, notes + 9 pay/CV pairs (`Table8.1a Full-Time`, `Table8.1b Full-Time CV`, …)               |
| Header row          | Row 5 (3 stacked header rows)   | Row 9 (single header row, after 8 rows of notes)                                                               |
| Percentile headers  | `10`, `20`, …                   | `10th percentile`, `20th percentile`, …                                                                        |
| Unreliable marker   | `x`                             | `[u]`                                                                                                          |
| Not available       | —                               | `[x]` (used for CVs of % changes)                                                                              |
| Not applicable      | `.` (CV files)                  | `[z]`                                                                                                          |
| Disclosive          | `..`                            | `[d]`                                                                                                          |
| Codes               | Prefixed with apostrophe        | Clean `N09…` codes                                                                                             |
| NI total row        | `Northern Ireland`, `N92000002` | `All employees`, code `[z]`                                                                                    |
| Row order           | Hierarchical                    | Alphabetical by name                                                                                           |
| Excel compatibility | Opens with openpyxl             | **openpyxl fails** (invalid colour values in the stylesheet). Read with `pandas.read_excel(engine="calamine")` |

The column order (Description, Code, Number of jobs, Median, change, Mean, change, 10 percentiles) is identical, so after header and marker normalisation both sources map to the same schema.

### Key Fields

Same as Section 3: `area_name`, `area_code`, `job_count_thousands`, `median_pay_gbp`, `median_annual_change_pct`, `mean_pay_gbp`, `mean_annual_change_pct`, `p10`–`p90`, plus `*_cv_pct` from the CV sheet.

### Findings (Full-Time, 2026)

- **All 11 LGDs are present**, with codes N09000001–N09000011 matching the population estimates.
- **Every LGD has a median for both weekly and annual pay.** None are suppressed.
- **Quality is good.** Weekly median CVs range from 2.6% to 5.7%, and annual from 3.9% to 6.7%. That puts every LGD in the "precise" or "reasonably precise" bands, which is better than many English districts.
- **The 90th percentile is `[u]` for every LGD.**
- Annual full-time medians range from £33,694 (Causeway Coast and Glens) to £42,678 (Lisburn and Castlereagh).

### Known Limitations

- **The NISRA NI total does not match the ONS NI row.** The ONS Table 8 row for Northern Ireland (N92000002) is not the same as NISRA's "All employees" total:

| Full-time, 2026 | ONS (N92000002) | NISRA (All employees) |
| --------------- | --------------- | --------------------- |
| Weekly median   | £760.5          | £754.4                |
| Annual median   | £38,482.5       | £38,203.4             |
| Jobs (weekly)   | 720k            | 699k                  |
| Jobs (annual)   | 601k            | 584k                  |

The job counts differ too, so the two producers' processing/weighting differs. They are separate official estimates and should not be mixed at the same geographic level.

- Same survey limitations as Section 3: provisional estimates, indicative job counts, and annual pay covering a different population from weekly pay.

### Data Quality Rules

| Issue                              | Handling                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| openpyxl cannot read the workbooks | Use the `calamine` engine. Add a test that each workbook opens                                                           |
| Header at row 9, notes above       | Locate the header row by finding `Description` in column A, not a fixed row number                                       |
| `[u]`, `[x]`, `[z]`, `[d]` markers | Map to the same `suppression_reason` values used for ONS (`unreliable`, `not_available`, `not_applicable`, `disclosive`) |
| Pay and CV on separate sheets      | Join on `area_code` within the workbook                                                                                  |
| NI total has code `[z]`            | Exclude from the local authority fact. Use the ONS N92 row for country-level comparisons                                 |
| Percentile header text             | Normalise `10th percentile` → `p10`                                                                                      |

### Modelling Implications

- **Combine NISRA LGDs with ONS lower-tier local authorities** in `fact_earnings` to cover all 361 local authorities. Add a `source` column (`ONS` / `NISRA`).
- **Country totals come from ONS only** (N92000002), so the four UK countries are compared on one consistent basis. NISRA's own NI total is not loaded as N92.
- **One parser, two source configurations.** A shared parser with a per-source config (header detection, marker map, CV location) is cleaner than two separate scripts, and is a good design point to show.
