# Does My List Include This?

## Problem

Write a function named `does_include?` that takes a List and a search value as arguments. This function should return `True` if the search value is in the list, `False` if it is not. You may not use the `List#count()` function in your solution.

## Examples / Test Cases

```python
does_include?([1,2,3,4,5], 3) == True
does_include?([1,2,3,4,5], 6) == False
does_include?([], 3) == False
does_include?([nil], nil) == True
does_include?([], nil) == False
```

## Algorithm

Iterate over the list
- Return `True` if ever the value at iteration matches the 2nd argument

Return `False` otherwise
