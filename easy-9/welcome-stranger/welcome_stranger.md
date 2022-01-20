# Welcome Stranger

## Problem

Create a function that takes 2 arguments, an list and a dictionary. The list will contain 2 or more elements that, when combined with adjoining spaces, will produce a person's name. The dictionary will contain two keys, `:title` and `:occupation`, and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title and occupation.

### Understanding

Input
- 2 arguments
	1. List
		- 2 or more elements
		- Strings
		- Represent a name
	2. Dictionary
		- Keys
			- `title`
			- `occupation`
		- Values
			- Strings
Output
- String
	- Greeting
	- Contains name, title, and occupation

## Examples / Test Cases

```python
greetings(['John', 'Q', 'Doe'], { 'title': 'Master', 'occupation': 'Plumber' })
#=> Hello, John Q Doe! Nice to have a Master Plumber around.
```

## Data Structures

- N / A

## Algorithm

1. Join names
2. Interpolate name, title, and occupation into string
3. Return greeting
