WITH min_size_table AS (
  SELECT
    MAX(sizes_raw_json.style_69879) AS "min_list" 
  FROM silver_runningwarehouse
)
SELECT 
  s1.min_list,
  s2.link
FROM min_size_table s1
JOIN silver_runningwarehouse s2 
ON s1.min_list = s2.sizes_raw_json.style_69879;


WITH min_val AS (
  SELECT MIN(LIST_MIN(sizes_raw_json.style_69879)) AS "min_value"
  FROM silver_runningwarehouse
)
SELECT s.link, s.sizes_raw_json.style_69879
FROM silver_runningwarehouse s
JOIN min_val m
ON list_contains(s.sizes_raw_json.style_69879, m.min_value) 
