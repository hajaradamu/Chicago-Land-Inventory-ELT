-- models/dim_address.sql

WITH source AS (
  -- Assuming 'api_data' is the source table from your API
  SELECT
    suffix_direction,
    min_address,
    suffix,
    max_address,
    street,
    full_street_name,
    direction
  FROM raw.api_data
)

SELECT
  suffix_direction,
  min_address,
  suffix,
  max_address,
  street,
  full_street_name,
  direction
FROM source;
