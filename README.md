# Chicago-Street-Names-ELT

##Overview

This project develops a scalable and automated data pipeline to ingest, transform, and analyze Chicago street names data from the Chicago Street Names API. The goal is to create valuable insights and metrics relevant to various stakeholders and support informed decision-making within the city.

##Data

The project utilizes the Chicago Street Names API dataset, which provides a comprehensive list of all Chicago streets with suffixes and minimum and maximum address numbers. The dataset includes the following columns:

name: The name of the street
address: The address of the street
full_street_direction: The full street direction, including the suffix (e.g., 1645 MIDWAY IE MIDWAYE)
suffix_diremin_addr: The suffix and directional identifier (e.g., IE MIDWAYE)
max_addr: The maximum address number for the street
min_addr: The minimum address number for the street

##Tools and Technologies

The project leverages the following tools and technologies:

Airflow: A workflow management platform for data pipelines
PostgreSQL: A relational database management system
Google Cloud Storage (GCS): A cloud storage service
Google BigQuery: A cloud data warehouse
dbt (data build tool): A tool for building and maintaining data transformations

##Project Stages

The project is divided into the following stages:

Data Extraction and Loading: Extract data from the Chicago Street Names API and load it into a PostgreSQL database.
Data Transformation and Integration: Transform and load data from PostgreSQL to Google Cloud Storage (GCS) and Google BigQuery.
Transformation Layer and Analytics Modeling: Develop a transformation layer in dbt and create analytics metrics models.

##Accomplishments

Upon successful completion of the project, the following accomplishments will be achieved:

A robust and automated data pipeline for ingesting, transforming, and analyzing Chicago street names data
A scalable and reliable data warehouse in Google BigQuery for efficient analysis
A transformation layer in dbt with diverse metrics to support various use cases
At least two analytics metrics models demonstrating the value addition of data engineering and analytics

##Benefits

The project will benefit various stakeholders in the city of Chicago, including:

City planners and policymakers: Gain valuable insights into the city's street network and address system for informed decision-making.
Public safety officials: Improve emergency response times and resource allocation by identifying areas with high address density or complex street layouts.
Businesses and developers: Enhance real estate analysis and valuation, optimize delivery routes, and improve customer service by better understanding the city's street network.
Citizens: Access interactive dashboards and visualizations to explore the city's street network and learn about their neighborhoods.

##Usage

To use the project, follow these steps:

Set up Airflow, PostgreSQL, Google Cloud Storage, Google BigQuery, and dbt.
Clone the project repository and configure the Airflow pipeline.
Start the Airflow pipeline to extract, transform, and load the data.
Develop and run analytics queries in BigQuery to explore and analyze the data.

##Conclusion

This ELT project provides a valuable example of how to use data engineering tools and techniques to create and manage data pipelines in a cloud environment. The project also demonstrates the potential of data analytics to support informed decision-making and improve various aspects of city life.
