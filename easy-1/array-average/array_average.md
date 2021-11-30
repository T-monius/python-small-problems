# array_average.md

## Problem

Write a method that takes one argument, an array containing integers, and returns the average of all numbers in the array. The array will never be empty and the numbers will always be positive integers. Your result should also be an integer.

### Understanding

Input
- One argument
	- List
		- Integer elements
Output
- Integer
	- Average of all of the numbers in the array
Python has a `reduce` built in method (correction `functools`)
- It takes a function and the list

Sum the elements
Divide by the length of the array / number of elements

## Examples / Test Cases

```ruby
puts average([1, 6]) == 3 # integer division: (1 + 6) / 2 -> 3
puts average([1, 5, 87, 45, 8, 8]) == 25
puts average([9, 47, 23, 95, 16, 52]) == 40
```

## Data Structures

- List

## Algorithm
### Functional Abstractions
- Reduction

### Hard Algorithm
- Sum the list with `reduce`
- Divide the sum by the length of the array
	- Get integer value