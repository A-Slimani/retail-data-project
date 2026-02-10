WITH products_unnested AS (
  SELECT 
    UNNEST(products) AS product  
  FROM read_json_auto('gs://retail-data-bucket-01/mmafightstore-wrestling-shoes/' || STRFTIME(CURRENT_DATE, '%Y-%m-%d') || '.json')
),
variants_unnested AS (
  SELECT
    product.title AS name,
    product.handle AS handle,
    UNNEST(product.variants) AS variant
  FROM products_unnested
)
SELECT
  variant.id AS id,
  name,
  CAST(variant.price AS DOUBLE) AS price,
  variant.option2 AS size,
  variant.available AS availability,
  'https://mmafightstore.com.au/products/' || handle AS product_link,
  variant.featured_image.src AS image_link
FROM variants_unnested 
