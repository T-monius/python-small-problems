# Reverse the Digits In a Number

## Problem

Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

### Understanding

Input
- Positive integer
Output
- Number
	- Reversed digits of input

## Examples / Test Cases

```python
reversed_number(12345) == 54321
reversed_number(12213) == 31221
reversed_number(456) == 654
reversed_number(12000) == 21 # No leading zeros in return value!
reversed_number(12003) == 30021
reversed_number(1) == 1

# 12345

num = 12345
mod = 10
digits = [5, 4, 3, 2, 1]
# 	      ^

num, rem = divmod(num, mod)
# rem = 5
# num = 1234
# ...

multiplier = 10000
total = 54321
```

## Data Structures

- List

## Algorithm

1. Assign input number to a new value num1
2. Declare `mod` variable
3. Declare an empty array for digit elements
4. While `num1` is greater than `0`
5.   Perform `divmod` `mod` on `num1`
6. 	 Append `rem` to `digits`
7. Declare a `multiplier` variable and assign `1`
8. Declare a `total` variable assigning `0`
9. Declare an `idx` variable one less than `digits` length
10. While `idx` is positive
11.   Access digit at iteration
12.   Multiply digit by multiplier and add to `total`
13.   Decrement `idx`
14. Return `total`
