# Unlucky Days

## Problem

Write a function that returns the number of Friday the 13ths in the year given by an argument. You may assume that the year is greater than 1752 (when the United Kingdom adopted the modern Gregorian Calendar) and that it will remain in use for the foreseeable future.

### Understanding

Input
- Integer
	- Year
Output
- Integer
	- Number of Friday the 13ths

Could come up with some complex pattern
- Friday the 13th occurs
- Days in Months
	- 30
	- 31
	- 28
	- 29

Could query 13ths of each month to determine whether Friday

## Examples / Test Cases

```python
friday_13th_count(2015) == 3
friday_13th_count(1986) == 1
friday_13th_count(2019) == 2
```

## Data Structures

- Date
- Range

## Algorithm

1. Set a `FRIDAY_INT` constant to `4`
2. Set `friday_13ths` to `0`
3. Iterate a range from `1` to `12`
4.   Create a date for the thirteenth of that month with input year
5.   Conditionally increment count if its a Friday
6. Return count
