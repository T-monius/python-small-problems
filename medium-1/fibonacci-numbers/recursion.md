# Fibonacci Numbers (Recursion)

## Problem

The Fibonacci series is a sequence of numbers starting with 1 and 1 where each number is the sum of the two previous numbers: the 3rd Fibonacci number is 1 + 1 = 2, the 4th is 1 + 2 = 3, the 5th is 2 + 3 = 5, and so on. In mathematical terms:

```
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2) where n > 2
```

Sequences like this translate naturally as "recursive" methods. A recursive method is one in which the method calls itself. For example:

```python
def sum(n):
    '''Return the sum of a number and all previous integers from 1'''
    if n == 1:
        return 1

    return n + sum(n - 1)
end
```

`sum` is a recursive method that computes the sum of all integers between 1 and n.

Recursive methods have three primary qualities:

1. They call themselves at least once.
2. They have a condition that stops the recursion (n == 1 above).
3. They use the result returned by themselves.

In the code above, `sum` calls itself once; it uses a condition of `n == 1` to stop recursing; and, `n + sum(n - 1)` uses the return value of the recursive call to compute a new return value.

Write a recursive function that computes the `nth` Fibonacci number, where `nth` is an argument to the function.

### Understanding

A number in the Fibonacci series is the sum of the two numbers previous.
Must user recursion
- Recursion requires a base case
	- Input number is `1` OR `2`

Input
- Integer
	- Represents a position in the Fibonacci series
	- `nth` number
- Output
	- The value at nth position

## Examples / Test Cases

```python
recursive_fibonacci(1) == 1
recursive_fibonacci(2) == 1
recursive_fibonacci(3) == 2
recursive_fibonacci(4) == 3
recursive_fibonacci(5) == 5
recursive_fibonacci(12) == 144
recursive_fibonacci(20) == 6765

n = 4

# (fib(4 - 1) OR 2) + (fib(4 - 2) OR i.e. 1)
# 2 + 1
n = 3

# (fib(3 - 1) OR 1) + (fib(3 - 2) OR 1) => 2
n = 2

# 1

```

## Data Structures

- N/A

## Algorithm

1. Write a guard clasus to represent the base case of `n == 1 or n == 2`
2. Recursively call the function to sum the values of two previous numbers in the series

### Bonus

1. Add caching
2. Implement tail recursion
