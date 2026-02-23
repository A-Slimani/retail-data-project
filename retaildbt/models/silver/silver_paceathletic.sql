WITH unnested_t AS (
  SELECT UNNEST(products, recursive := true) AS products
  FROM read_json_auto('gs://retail-data-bucket-01/pace-athletic/*.json')
)
SELECT
  id,
  title,
  created_at,
  updated_at,
  vendor,
  product_type,
  price::DOUBLE AS "price",
  REGEXP_EXTRACT(size, 'US\s*(?:M\s*)?(\d+(?:\.\d+)?)', 1)::DOUBLE AS "size",
  colour,
  availability,
  link,
  scraped_at
FROM unnested_t

