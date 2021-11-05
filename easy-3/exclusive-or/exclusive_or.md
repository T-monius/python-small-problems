# Exclusive Or

## Problem

The || operator returns a truthy value if either or both of its operands are truthy. If both operands are falsey, it returns a falsey value. The && operator returns a truthy value if both of its operands are truthy, and a falsey value if either operand is falsey. This works great until you need only one of two conditions to be truthy, the so-called exclusive or.

In this exercise, you will write a function named xor that takes two arguments, and returns True if exactly one of its arguments is truthy, false otherwise. Note that we are looking for a boolean result instead of a truthy/falsy value as returned by || and &&.

### Understanding

One and only one of two arguments must be `True`

## Examples / Test Cases

True, True   => False
True, False  => True
False, True  => True
False, False => False

```python
is_xor(is_even(5), is_even(4)) == True
is_xor(is_odd(5), is_odd(4)) == True
is_xor(is_odd(5), is_even(4)) == False
is_xor(is_even(5), is_odd(4)) == False
```

## Algorithm
### Functional Abstractions
- Interrogaton

### Hard Algorithm
- Write `is_odd` and `is_even` functions
- If first argument is True
  - If second argument is False
    - Return True
- If Second Argument is True
  - If first argument is False
    - Return True
- Else Return False
