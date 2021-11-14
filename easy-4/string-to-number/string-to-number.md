# Convert a String to a Numeber!

## Problem

Write a function that takes a String of digits, and returns the appropriate number as an integer. You may not use any built in conversion methods.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters will be numeric.

You may not use any of the standard conversion methods available in Python. Your function should do this the old-fashioned way and calculate the result by analyzing the characters in the string.

### Understanding

- `ord` will give the ASCII value of a character
- A dictionary will maintain name, value pairs

## Examples / Test Cases

```python
string_to_integer('4321') == 4321
string_to_integer('570') == 570

'4321'

end_idx = 3
index_multiplier = 0
current_char = 1
num = 1
multiplier = 10 ** 0 #=> 1
total = (1 * 1)
```

## Data Structures

- Dictionary

## Algortihm
### Functional Abstractions

- Transformation

### Hard Algorithm

- Create a dictionary of int and string digits
- Instantiate a `total` variable
- Declare a variable for length
- Declare a varibale for multiplying by 10
- Iterate backwards
  - Access current char
  - Get conversion
  - Multiply conversion by index multiplier
  - Add to total
- Return total
