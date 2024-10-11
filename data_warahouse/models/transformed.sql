{{ config(materialized='table') }}

WITH filtered_sales AS (
    SELECT *
    FROM {{ source('public', 'data_warahouse') }}
    WHERE Quantity > 0
    AND UnitPrice > 0
)

SELECT
    InvoiceNo,
    StockCode,
    Description,
    Quantity,
    UnitPrice,
    Quantity * UnitPrice AS TotalAmount,
    InvoiceDate,
    CustomerID,
    Country
FROM filtered_sales
