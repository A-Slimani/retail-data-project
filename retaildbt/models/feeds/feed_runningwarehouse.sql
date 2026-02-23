SELECT
  model_number,
  name,
  link,
  colour,
  price,
  scraped_at,
  size
FROM {{ ref('silver_runningwarehouse')}}
WHERE 
  size=9
  AND
  scraped_at=CURRENT_DATE
ORDER BY price

