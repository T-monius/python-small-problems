# What Century is That?

## Problem

Write a method that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with st, nd, rd, or th as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901-2000 comprise the 20th century.

### Understanding

Input
- Year
  - Integer
Output
- String
  - Century of the numer
  - Proper suffix

Ordinal Numbers
- Suffixes
  - 1, 2, 3 are unique
  - 4-10 are 'th'
  - 11, 12, 13 are 'th'
  - All teens are 'th'
  - Greater and eual to 20
    - Numbers follow the same pattern as 0-10

## Examples / Test Cases

```python
century_for_numeric_year(2000) == '20th'
century_for_numeric_year(2001) == '21st'
century_for_numeric_year(1965) == '20th'
century_for_numeric_year(256) == '3rd'
century_for_numeric_year(5) == '1st'
century_for_numeric_year(10103) == '102nd'
century_for_numeric_year(1052) == '11th'
century_for_numeric_year(1127) == '12th'
century_for_numeric_year(11201) == '113th'
```

Years between 1 and 100 are the first century
- Kind of an off by one
  - If you divide the number by 100, the century will be one greater than the number of quotient
    - Except, if the number is evenly divided by 100

## Data Structures

- N/A

## Algorithm

1. Declare `century_count`
2. Number a multiple of 100?
  - a. Set it as the `century_count`
  - b. Get integer division of number by 100
    - add 1 set quotient as `century_count`
3. Get the remainder of century division
  - If number is greater than 19
    - Get remainder of 10 division
    - Treat like a number between one and ten
  - Return suffix for 0-10
  - Return suffix for pre-teens and teens
4. Concatenate century count and suffix
