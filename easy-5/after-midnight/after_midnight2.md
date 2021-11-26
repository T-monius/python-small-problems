# After Midnight (Part 2)

## Problem

As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0..1439.

You may not use ruby's Date and Time functions.

### Understanding

Time AS number of minutes before OR after midnight
2 functions

Input
- String
  - Time of day
  - 24 hr format
Output
- Integer
  - Number of minutes

After midnight represents minutes into current day
- Just calculate total minutes
Before midnight represents minutes until the next
- Calculate total minutes
- Subtract from total minutes in day

## Examples / Test Cases

```python
after_midnight('00:00') == 0
before_midnight('00:00') == 0
after_midnight('12:34') == 754
before_midnight('12:34') == 686
after_midnight('24:00') == 0
before_midnight('24:00') == 0
```

## Data Structures

- N/A

## Algorithm
### After midnight
- Split string from colon
  - Assign `hrs` and `mins` variables
  - Coerce vars to `int`
- Convert `hrs` to minutes AND add to `mins`
### Before midnight
- Calculate `after_midnight`
- Subtract from `TOTAL_MINUTES_IN_DAY` (i.e. 1440)
