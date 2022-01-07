# Fizz Buzz

## Problem

Write a function that takes two arguments: the first is the starting number, and the second is the ending number. Print out all numbers between the two numbers, except if a number is divisible by 3, print "Fizz", if a number is divisible by 5, print "Buzz", and finally if a number is divisible by 3 and 5, print "FizzBuzz".

### Understanding

Input
- Two arguments
  - Numbers
    - Starting
    - Ending
Output
- StdOut
- Or, Sring, list
  - All numbers in range from `start` up to `end` inclusive
  - Exceptions
    - Number is divisible by Five and Three
      - 'FizzBuzz'
    - Number is divisible by Five only
      - 'Buzz'
    - Number is divisible by Three only

## Examples / Test Cases

```python
 fizzbuzz(1, 15) # -> 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

start = 1
end = 15

fizzbuzz = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
```

## Data Structures

- List

## Algorithm

- Declare and empty list `fizzbuzz`
- For a range between `start` and `end` (plus one) parameters
  - If the number is divisible by 5
    - If it's also divisible by 3
      - Append `FizzBuzz` to the return list
    - Else
      - Append `Fizz`
  - Else if the number is divisible by 3
    - Append `'Buzz'` to the return list
  - Else
    - Append the number itself to the return list
- Return the list `fizzbuzz`
