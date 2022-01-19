'''A module for working with the digits of numbers'''

def reversed_digits_with(num):
    '''Return a list of digits from an input number. The list is in
       reverse order of appearance in the original number.'''
    num1 = num
    mod = 10
    digits = []

    while num1 > 0:
        num1, rem = divmod(num1, mod)
        digits.append(rem)

    return digits


def compose_number(digits):
    '''Return a number composed of the numeric elements of a list'''
    multiplier = 1
    total = 0
    idx = len(digits) - 1

    while idx >= 0:
        dig = digits[idx]
        dig *= multiplier
        total += dig
        multiplier *= 10
        idx -= 1

    return total


def reversed_number(num):
    '''Return the number value of the input number with its digits in
       reverse'''
    digits = reversed_digits_with(num)
    backwards = compose_number(digits)

    return backwards
