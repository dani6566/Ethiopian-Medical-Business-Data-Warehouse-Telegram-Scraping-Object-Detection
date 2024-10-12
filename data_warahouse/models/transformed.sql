{{ config(materialized='table') }}

WITH raw_data AS (
    SELECT *
    FROM {{ ref('data_warehouse') }}  -- Reference to the raw data source
)

SELECT 
    id,
    UPPER(channel_title) AS channel_title,   -- Transform channel_title to uppercase
    channel_username,
    message,
    date,
    media_path
FROM raw_data
WHERE id IS NOT NULL  -- Ensure the id is not null
