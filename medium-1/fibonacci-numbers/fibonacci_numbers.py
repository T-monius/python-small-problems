'''A module for working with numbers in the Fibonacci Series'''

def recursive_fibonacci(num):
    '''Calculate the nth number in the Fibonacci series based on input
       num recursively'''
    if num in (1, 2):
        return 1

    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)
