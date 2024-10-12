
{{ config(materialized='table') }}

SELECT *
FROM public.data_warehouse
