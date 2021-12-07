# Cute Angles

## Problem

Write a function that takes a floating point number that represents an angle between 0 and 360 degrees and returns a string that represents that angle in degrees, minutes and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. A degree has 60 minutes, while a minute has 60 seconds.

### Understanding

Input
- Single argument
	- Float
Output
- String
	- Degrees, Minutes, Seconds
	- Symbols

60 minutes in a degree
60 seconds in a minute

## Examples / Test Cases

```python
dms(30) == "30°00'00\""
dms(76.73) == "76°43'48\""
dms(254.6) == "254°36'00\""
dms(93.034773) == "93°02'05\""
dms(0) == "0°00'00\""
dms(360) == "360°00'00\"" || dms(360) == "0°00'00\""

fl = 76.73
degrees = 70 # int value of fl
rem = .73.   # fl % 1
rem * 60 = minutes_fl
minutes = int(minutes_fl)
minutes_fl % 1 = rem
rem * 60 = seconds
```

## Data Structres

- N/A

## Algorithm
### Functional Abstractions
- N/A

### Steps
1. Declare `degrees` variable assigning int value of input
2. Set `rem` variable to mod of 1 from input
3. Calculate `minutes` by multiplying `rem` by 60
4. Re-caluculate `rem` by finding mod 1 of `minutes`
5. Calculate `seconds` by multiplying `rem` by 60
6. Re-assign `minutes` and `seconds` to int values of themselves
7. Coerce values into strings
8. Invoke `zfill` of 2 on string values interpolating into return string
