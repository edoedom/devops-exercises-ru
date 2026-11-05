SELECT COUNT(*) AS purchases_in_2017
FROM shawarma_purchases
WHERE purchased_at >= '2017-01-01'
  AND purchased_at < '2018-01-01';
