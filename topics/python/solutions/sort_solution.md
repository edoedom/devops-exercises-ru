<a id="sort-descending---solution"></a>
## Сортировка по убыванию: решение

1. Напишите функцию, которая сортирует следующий список списков по убыванию без `sorted()` и `.sort()`:

   - mat_list = [[1, 2, 3], [2, 4, 4], [5, 5, 5]] -> [[5, 5, 5], [2, 4, 4], [1, 2, 3]]

```python
def sort_desc(mat: list) -> list:
    """ Sorts a list in descending order

    Args:
        mat (list): paresd list

    Returns:
        list: A new list
    """
    new_list = []
    while mat != []:
        maxx = max(mat)
        new_list.append(maxx)
        mat.remove(maxx)
    return new_list

print(sort_func(mat_list))
```
