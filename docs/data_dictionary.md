# Data Dictionary

## 1. Purpose

This document defines the fields, data types and business meanings used within the UK Housing Intelligence Platform.

It will act as a reference for the structure of source datasets and the standardised data models created during transformation.

The dictionary will evolve as additional data sources and database models are introduced.

## 2. Naming Conventions

The project will use the following conventions for standardised database fields:

- Lowercase column names.
- Snake_case naming convention.
- Dates stored using appropriate SQL date types.
- Monetary values stored as numeric values.
- Geographical identifiers retained as source codes where possible.
- Percentage values represented consistently.

## 3. UK House Price Index

The following fields represent the proposed standardised structure for house price observations.

| Field              | Data Type | Description                                                          |
| ------------------ | --------- | -------------------------------------------------------------------- |
| reference_date     | DATE      | Date or period the observation relates to                            |
| area_code          | VARCHAR   | Official geographical identifier                                     |
| area_name          | VARCHAR   | Name of the geographical area                                        |
| average_price      | NUMERIC   | Average residential property price in GBP                            |
| price_index        | NUMERIC   | House price index value                                              |
| annual_change      | NUMERIC   | Percentage change compared with the same period in the previous year |
| monthly_change     | NUMERIC   | Percentage change compared with the previous month                   |
| observation_status | VARCHAR   | Status of the observation, such as provisional or revised            |

## 4. Future Data Sources

Additional field definitions will be added as the following datasets are integrated:

- Private rental prices.
- Annual earnings.
- Population estimates.
- Bank of England interest rates.

## 5. Notes

The fields above describe the proposed standardised data model rather than the exact column names in the original source files.

Source-specific fields and transformations will be documented as the ingestion and transformation processes are developed.
