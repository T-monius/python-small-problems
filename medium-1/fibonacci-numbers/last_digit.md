# Fibonacci Numbers (Last Digit)

## Problem

In the previous exercise, we developed a procedural function for computing the value of the `nth` Fibonacci number. This function was really fast, computing the 20899 digit 100,001st Fibonacci sequence almost instantly.

In this exercise, you are going to compute a function that returns the last digit of the `nth` Fibonacci number.

### Understanding

The last digit of a number can be derived mathematically by getting the modulus of 10 division or by casting to a string.
- Can a very large number be coerced to a string
- Are there problems dividing very large numbers

## Examples / Test Cases

```python
fibonacci_last(15)        # -> 0  (the 15th Fibonacci number is 610)
fibonacci_last(20)        # -> 5 (the 20th Fibonacci number is 6765)
fibonacci_last(100)       # -> 5 (the 100th Fibonacci number is 354224848179261915075)
fibonacci_last(100_001)   # -> 1 (this is a 20899 digit number)
fibonacci_last(1_000_007) # -> 3 (this is a 208989 digit number)
fibonacci_last(123456789) # -> 4

nth = 15
'''
num = 610
rem = 610 % 10 => 0
'''

nth = 20
'''
num = 6765
6765 % 10 => 5
'''
```

## Data Structures

- N/A

## Algorithm

