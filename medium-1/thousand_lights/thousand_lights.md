# 1000 Lights

## Problem

You have a bank of switches before you, numbered from 1 to n. Each switch is connected to exactly one light that is initially off. You walk down the row of switches and toggle every one of them. You go back to the beginning, and on this second pass, you toggle switches 2, 4, 6, and so on. On the third pass, you go back again to the beginning and toggle switches 3, 6, 9, and so on. You repeat this process and keep going until you have been through n repetitions.

Write a function that takes one argument, the total number of switches, and returns a List that identifies which lights are on after `n` repetitions.

## Understanding

Bank of Switches
- Switches
	- Numbered
		- 1 to n

Lights
- Connected to 1 switch
- Starts off

Walk
1. Toggle all switches, positions divisible by 1
2. Toggle switches whose position is divisible by two
3. Toggle every switch position divisible by 3
... Continue toggling incrementing positions up to `n`

## Examples / Test Cases

Example with n = 5 lights:

    round 1: every light is turned on
    round 2: lights 2 and 4 are now off; 1, 3, 5 are on
    round 3: lights 2, 3, and 4 are now off; 1 and 5 are on
    round 4: lights 2 and 3 are now off; 1, 4, and 5 are on
    round 5: lights 2, 3, and 5 are now off; 1 and 4 are on

The result is that 2 lights are left on, lights 1 and 4. The return value is [1, 4].

With 10 lights, 3 lights are left on: lights 1, 4, and 9. The return value is [1, 4, 9].

```python
n = 5
switch_bank = [True, False, True, False, True]
# 			                                   ^
walk = 2
idx = 4
# idx + 1 % walk == 0, True
# ... after five walks
switch_bank = [True, False, False, True, False]
# 		                     					       ^
on_switches = [1, 4]
idx = 3
```

## Data Structures

- List

## Algorithm

1. Populate a list, `switch_bank`, of booleans to `n` `False` elements
	- List comprehension
2. Iterate a range from `1` up to `n + 1` as `walk`
3.   Iterate over the `switch_bank` with an index
4.     Flip switch if `idx` plus `1` is divsible by `walk` (or, us step)
5. Declare an empy list `on_switches`
6. Iterate over `switch_bank` with index and value as `switch`
	- Append `idx` plus `1` to `on_swithes` if `switch` is `True`
7. Return `on_switches`

- WON'T WORK!!
	- Mutating a list while iterating over it
	- Introduce a dictionary instead
