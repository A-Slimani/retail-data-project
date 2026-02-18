SELECT
  model_number,
  name,
  link,
  colour,
  price,
  UNNEST(sizes_raw_json.style_69879) AS size,
  scraped_at
FROM read_json_auto('gs://retail-data-bucket-01/running-warehouse/*.json')

