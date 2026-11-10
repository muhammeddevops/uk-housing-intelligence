# Architecture

## 1. Project Overview

The UK Housing Intelligence Platform is a data engineering project designed to combine publicly available UK housing and economic datasets.

The platform will process data from multiple sources to support analysis of:

- Residential property price trends.
- Rental price trends.
- Housing affordability.
- Regional and local authority comparisons.
- The relationship between housing costs, earnings and population changes.

The objective is to build a reliable, repeatable and scalable data pipeline that transforms raw public data into structured datasets suitable for analytical reporting.

## 2. Technology Stack

| Technology                   | Purpose                                |
| ---------------------------- | -------------------------------------- |
| Python                       | Data extraction and ingestion          |
| Azure Data Lake Storage Gen2 | Cloud-based data storage               |
| PostgreSQL                   | Relational database storage            |
| dbt                          | SQL transformations and data modelling |
| Apache Airflow               | Pipeline orchestration and scheduling  |
| Docker                       | Containerisation and local development |
| pytest                       | Python testing                         |
| GitHub Actions               | Continuous integration                 |
| Power BI                     | Data visualisation and reporting       |

## 3. High-Level Architecture

The proposed data flow is:

1. Data is retrieved from official external sources.
2. Python ingestion scripts extract and validate the source data.
3. Original datasets are stored in Azure Data Lake Storage.
4. Structured data is loaded into PostgreSQL.
5. dbt transforms the data into analytical models.
6. Airflow orchestrates the pipeline and its dependencies.
7. Power BI connects to the final analytical datasets.

## 4. Data Storage Layers

The platform will follow a medallion-style architecture.

### Bronze Layer – Raw Data

Stores original source data with minimal modification.

Examples:

- Original Excel workbooks.
- CSV downloads.
- API responses.

### Silver Layer – Cleaned Data

Contains validated and standardised datasets.

Examples:

- Standardised date formats.
- Consistent geographical identifiers.
- Corrected data types.
- Duplicate handling.

### Gold Layer – Analytical Data

Contains business-ready datasets designed for reporting and analysis.

Examples:

- House price trends by local authority.
- Rental price and earnings comparisons.
- Housing affordability indicators.

## 5. Orchestration

Apache Airflow will coordinate the pipeline.

It will manage task dependencies, scheduling, execution and failure handling.

## 6. Development and Deployment Approach

Initial development will use Docker to run services locally, including PostgreSQL and Airflow.

Azure storage will be integrated as the cloud storage layer.

The project will prioritise low-cost development while maintaining an architecture that can be extended towards cloud-based deployment.

## 7. Architecture Status

This document describes the proposed architecture. Specific implementation details may change as data sources are validated and the pipeline is developed.
