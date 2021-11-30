# After Midnight

## Problem

The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a method that takes a time using this minute-based format and returns the time of day in 24 hour format (hh:mm). Your method should work with any integer input.

You may not use Python's Date and Time classes.

### Understanding

Time of day
- Minutes before OR after midnight
	- Positive = before
	- Negative = after
Input
- Time
	- Minutes
Output
- Time of day
- 24 hour format
	- (hh:mm)

60 minutes in an hours
24 hours in a day

1440 total minutes in a day
- Input minutes % minutes in a day returns current time in minutes
	- Before OR after midnight

## Examples / Test Cases



```python
time_of_day(0) == "00:00"
time_of_day(-3) == "23:57"
time_of_day(35) == "00:35"
time_of_day(-1437) == "00:03"
time_of_day(3000) == "02:00"
time_of_day(800) == "13:20"
time_of_day(-4231) == "01:29"
```

## Algorithms

1. Calculate hours then minutes for positive
- Divide total minutes by 60 to get total hours
	- Remainder is the minutes of the given / current hour
- Take the remainder of hours modulus 24 to get hours of current day
	- In case, there are several days worth of hours
(Only works for _Before_)

2. Take modulus of input minutes first
	1. Divmod _hours_ and _minutes_
	2. Calculate zeros
	3. Interpolate into string

Calculate zeros
- If string is length one, prepend zero
