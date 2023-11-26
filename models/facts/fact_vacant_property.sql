-- models/fact_vacant_property.sql

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
  WHERE -- Add any additional filters or conditions to identify vacant properties
    is_vacant = true
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
