# Counting the Number of Characters

## Problem

Write a program that will ask a user for an input of a word or multiple words and give back the number of characters. Spaces should not be counted as a character.

### Understanding

Implement w/o user input to test easier.
Input
- String
  - Phrase
    - One or more words
Output
- Count
  - Non-space charactes

Can use regex
Can use a dictionary
Can use ascii value?
- `ord`
- `chr`

## Examples / Test Cases

walk            => 4
walk, don't run => 13

## Data Structures

- String

## Algorithm
### Functional Abstractions
- Selection / Filter
- Or, reduction

### Filtering algorithm

- Split the word into an array
- Select characters that are non-whitespace
- Count array returned

### String Function

- Replace whitespaces w/ empty strings
- Count
