# Diamonds

## Problem

Write a function that displays a 4-pointed diamond in an n x n grid where `n` is an odd integer that is supplied as an argument to the method. You may assume that the argument will always be an odd integer.

### Understanding

Function
- Input
	- Integer
	- Odd
- Output
	- Grid
		- n x n
		- Print to StdOut

## Examples / Test Cases

```python
diamond(1)
# *

diamond(3)
'''
 *
***
 *
'''

otp = ' *\n***\n *'

diamond(5)
'''
  *
 ***
*****
 ***
  *
'''

otp1 = '  *\n ***\n*****\n ***\n  *\n'

dmd = '  *\n ***\n*****\n ***\n  *'
mid = int(n / 2)        			#=> 2

n = 5
line = 5
stars = 1
spaces = int((n - stars) / 2) #=> 2



'''

'''

otp2 = '  *\n ***\n*****\n ***\n  *'
```

## Data Structures

- String

## Algorithm

1. Instantiate a `dmd` variable to an empty string
1. Calculate `midpoint` (i.e. `int(n / 2)`)
2. ~~Set a `line` variable to `0`~~
3. Set a `stars` variable to `1`
4. Iterate a range from `0` up to `n` w/ val as `line`
5.   If `line` is less than or equal to `midpoint` and not `0`
6.     Add two to `stars`
7.   Else
       Subtract two from `starts`
8.   Calculate `spaces` from `stars` (i.e. `int((n - stars) / 2)`)
9.   Append spaces
10.  Append stars
11.  Append newline
12. Return `dmd`
