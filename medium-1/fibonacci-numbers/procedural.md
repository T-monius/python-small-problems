# Fibonacci Numbers (Procedural)

## Problem

In the previous exercise, we developed a recursive solution to calculating the `nth` Fibonacci number. In a language that is not optimized for recursion, some (not all) recursive methods can be extremely slow and require massive quantities of memory and/or stack space.

Python may or may not do a reasonably good job of handling recursion, but may not be designed for heavy recursion; as a result, the Fibonacci solution is only useful up to about `fibonacci(40)`. With higher values of `nth`, the recursive solution is impractical. (Our tail recursive solution did much better, but even that failed at around `fibonacci(8200)`.)

Fortunately, every recursive function can be rewritten as a non-recursive (procedural) function.

Rewrite your recursive fibonacci function so that it computes its results without recursion.

### Understanding

First two numbers in the series are `1` and `1`.
`nth` number is the value of the two previous.

## Examples / Test Cases

```python
fibonacci(20) == 6765
fibonacci(100) == 354224848179261915075
fibonacci(100_001) # => 4202692702.....8285979669707537501

prev = 2
two_prev = 1
position = 4
current_num = 3
nth = 4
```

## Data Structures

- N/A

## Algorithm

1. Conditionally return if `nth` is less than `3`
2. Set a variable for `prev`
3. Set a variable for `two_prev`
4. Set a `current_num` variable to `None`
4. Iterate a range from `3` up to one past `nth`
5.   Calculate `current_num`
6.   Set `prev` to `current_num`
7.   Set `two_prev` to `prev`
8. Return `current_num`
