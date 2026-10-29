<a id="comparisons-vs-functions---solution"></a>
## Сравнения и функции: решение

```
SELECT count(*)
FROM shawarma_purchases
WHERE
  purchased_at >= '2017-01-01' AND
  purchased_at <= '2017-31-12'
```
