SELECT 
  name,
  CAST(REPLACE(price, '$', '') AS DOUBLE) AS price,
  link
FROM read_json_auto('gs://retail-data-bucket-01/running-warehouse/*.json')

