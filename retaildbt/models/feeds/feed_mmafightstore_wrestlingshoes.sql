SELECT
  id,
  name,
  price,
  size,
  availability,
  product_link,
  last_updated_at
FROM {{ ref('silver_mmafightstore_wrestlingshoes')}}
WHERE 
  availability='true' 
  AND
  size=9
  AND
  last_updated_at=CURRENT_DATE
ORDER BY price

