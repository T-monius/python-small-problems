# Double Doubles

## Problem

A double number is a number with an even number of digits whose left-side digits are exactly the same as its right-side digits. For example, `44`, `3333`, `103103`, `7676` are all double numbers. `444`, `334433`, and `107` are not.

Write a function that returns 2 times the number provided as an argument, unless the argument is a double number; double numbers should be returned as-is.

### Understanding

Input
- Number
Output
- Input number
	- If the number is a double
- OR double the input number

Doubles
- Will be an even length
- Splitting an even length string and comparing slices before and after the middle will reveal a double

## Examples / Test Cases

```python
twice(37) == 74
twice(44) == 44
twice(334433) == 668866
twice(444) == 888
twice(107) == 214
twice(103103) == 103103
twice(3333) == 3333
twice(7676) == 7676
twice(123_456_789_123_456_789) == 123_456_789_123_456_789
twice(5) == 10
```

## Data Structures

- String

## Algorithm

1. Determine if the input number `is_double`
2.   Return the number if it's a double
3. Else
    - Double the number and return it

`is_double`
1. Coerce the input number to a string
2. Early return if the length is not even
3. Determine the midpoint
4. Slice the string to `up_to_mid` and `after_mid` slices
5. Compare slices
