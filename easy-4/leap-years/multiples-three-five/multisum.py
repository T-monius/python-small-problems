'''A module for working with multples of 3 and 5'''

def multisum(range_limit):
    multiples = []
    for num in range(1, range_limit + 1):
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)

    return sum(multiples)