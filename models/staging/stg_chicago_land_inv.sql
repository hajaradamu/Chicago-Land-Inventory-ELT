with source as (

    select * from {{ source('Chicago_Land_Inv', 'chicago_land_inventory') }}

)
    select
        suffix_direction,
        min_address,
        suffix,
        max_address,
        street,
        full_street_name,
        direction

    from source