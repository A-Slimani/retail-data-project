WITH size_code_t AS (
  SELECT
    model_number,
    name,
    link,
    colour,
    price::DECIMAL(10, 2) AS "price",
    UNNEST(sizes_raw_json.style_69879) AS size,
    scraped_at
  FROM read_json_auto('gs://retail-data-bucket-01/running-warehouse/*.json')
)
SELECT
  t.model_number,
  t.name,
  t.link,
  t.colour,
  t.price,
  t.scraped_at,
  s.size
FROM size_code_t AS t
JOIN {{ ref('shoe_size') }} s
ON t.size = s.code 

