'''A module for working with numbers in the Fibonacci Series'''

def recursive_fibonacci(nth):
    '''Calculate the nth number in the Fibonacci series based on input
       nth recursively'''
    if nth in (1, 2):
        return 1

    return recursive_fibonacci(nth - 1) + recursive_fibonacci(nth - 2)

def procedural_fibonacci(nth):
    '''Calculate the nth number in the Fibonacci seriese procedurally'''
    if nth < 3:
        return 1

    prev = 1
    two_prev = 1

    for _ in range(3, nth + 1):
        current_num = prev + two_prev
        two_prev = prev
        prev = current_num

    return current_num

def fibonacci_last(nth):
    num = procedural_fibonacci(nth)
    last_digit = num % 10

    return last_digit
