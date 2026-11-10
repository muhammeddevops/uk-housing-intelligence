# Data Quality

## 1. Purpose

This document defines the data quality standards and validation rules for the UK Housing Intelligence Platform.

The objective is to ensure that ingested and transformed datasets are accurate, complete, consistent and suitable for analytical use.

## 2. Data Quality Dimensions

The project will focus on the following dimensions:

| Dimension    | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| Completeness | Required fields should not contain unexpected missing values |
| Accuracy     | Values should fall within reasonable and valid ranges        |
| Consistency  | Data formats and definitions should be standardised          |
| Uniqueness   | Records should not contain unintended duplicates             |
| Validity     | Values should conform to expected formats and rules          |
| Timeliness   | Data should reflect the latest available source publication  |

## 3. Initial Validation Rules

### UK House Price Index

| Check                                          | Expected Result                                     |
| ---------------------------------------------- | --------------------------------------------------- |
| Missing geographical identifiers               | None                                                |
| Duplicate area and reference date combinations | None within the same measure                        |
| Average house prices                           | Greater than zero where an observation is available |
| Reference dates                                | Valid dates                                         |
| Annual and monthly changes                     | Valid numeric values                                |
| Observation status                             | Valid status or explicitly recorded as unavailable  |
| Geographical identifiers                       | Match recognised geographical codes                 |

## 4. Source-Specific Considerations

The UK House Price Index contains several characteristics that must be handled correctly:

- Some recent observations are provisional and may be revised.
- Northern Ireland local authority figures are quarterly.
- Some supplementary measures have different geographical coverage.
- Unavailable observations must be distinguished from missing or invalid records.

## 5. Pipeline Validation

Data quality checks will be implemented at different stages of the pipeline.

### Ingestion

- Confirm that downloaded files are valid.
- Check that expected worksheets or columns exist.
- Validate file size and reporting period.

### Transformation

- Validate data types.
- Standardise geographical identifiers.
- Handle missing and unavailable values.
- Identify duplicate records.
- Validate numerical ranges.

### Analytical Models

- Test primary key uniqueness.
- Test required fields for null values.
- Validate relationships between tables.
- Check that derived metrics follow their documented definitions.

## 6. Testing Tools

The project intends to use:

- pytest for Python ingestion and validation tests.
- dbt tests for transformed datasets.
- Airflow task monitoring for pipeline execution and failures.

## 7. Future Improvements

Additional validation rules will be introduced as new datasets are integrated and actual data quality issues are identified.
