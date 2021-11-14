# Leap Years

## Problem

In the modern era under the Gregorian Calendar, leap years occur in every year that is evenly divisible by 4, unless the year is also divisible by 100. If the year is evenly divisible by 100, then it is not a leap year unless the year is evenly divisible by 400.

Assume this rule is good for any year greater than year 0. Write a method that takes any year greater than 0 as input, and returns `True` if the year is a leap year, or `False` if it is not a leap year.

### Understanding

- Modern leap year
  - Evenly divisible by four
    - __UNLESS__ divisible by 100
  - OR, divisible by 100 and 400
  - __SO__
    1. Test greater than 0
    2. Test _divisibility by 400_
    3. _divisibility by 100_
    4. Divisible by 4?

## Examples / Test Cases

```python
is_leap_year(2016) == True
is_leap_year(2015) == False
is_leap_year(2100) == False
is_leap_year(2400) == True
is_leap_year(240000) == True
is_leap_year(240001) == False
is_leap_year(2000) == True
is_leap_year(1900) == False
is_leap_year(1752) == True
is_leap_year(1700) == False
is_leap_year(1) == False
is_leap_year(100) == False
is_leap_year(400) == True
```

## Problem 2


A continuation of the previous exercise.

The British Empire adopted the Gregorian Calendar in 1752, which was a leap year. Prior to 1752, the Julian Calendar was used. Under the Julian Calendar, leap years occur in any year that is evenly divisible by 4.

Using this information, update the method from the previous exercise to determine leap years both before and after 1752.

### Understanding

Prior to 1752, every year divisible by 4 affirmative
After, modern treatment

Conditionally use old 'method'

## Examples / Test Cases

```python
is_leap_year(2016) == true
is_leap_year(2015) == false
is_leap_year(2100) == false
is_leap_year(2400) == true
is_leap_year(240000) == true
is_leap_year(240001) == false
is_leap_year(2000) == true
is_leap_year(1900) == false
is_leap_year(1752) == true
is_leap_year(1700) == true
is_leap_year(1) == false
is_leap_year(100) == true
is_leap_year(400) == true
```
