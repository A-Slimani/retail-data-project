SELECT 
  title,
  vendor,
  price,
  size, 
  availability,
  link
FROM {{ ref('silver_paceathletic') }}
WHERE 
  product_type IN ('Neutral Daily Trainers', 'Tempo Trainers', 'Stability Trainers', 'Road Racing Shoes')
  AND
  size=9
  AND
  scraped_at=CURRENT_DATE
  AND
  availability='true'


