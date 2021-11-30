# Sum of Digits

## Problem

Write a method that takes one argument, a positive integer, and returns the sum of its digits.

### Understanding

Input
- Single Integer
Output
- Sum of its digits

Can retrieve the digits of an integer with modulus
Or, can retrieve by converting to a sting and splitting

## Examples / Test Cases

23 => 5
496 => 19
123_456_789 => 45

## Data Structures

- String
- List

## Algorithm
### Functional Abstractions
- Map
- Reduce

### Hard Algorithm
- Convert to a string
- Coerce to a list fromt the string
- Map the list to integers
	- Convert the iterator object to a list
- Reduce the integers to a total
