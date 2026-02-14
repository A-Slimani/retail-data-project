WITH products_unnested AS (
  SELECT 
    UNNEST(products) AS product
  FROM read_json_auto('gs://retail-data-bucket-01/mmafightstore-wrestling-shoes/*.json')
),
variants_unnested AS (
  SELECT
    product.title AS name,
    product.handle AS handle,
    CAST(product.updated_at AS DATE) AS last_updated_at, 
    UNNEST(product.variants) AS variant
  FROM products_unnested
)
SELECT
  variant.id AS id,
  name,
  last_updated_at,
  CAST(variant.price AS DOUBLE) AS price,
  REGEXP_EXTRACT(variant.option2, '[0-9]+(\.[0-9]+)?') AS size,
  variant.available AS availability,
  'https://mmafightstore.com.au/products/' || handle AS product_link
FROM variants_unnested 

