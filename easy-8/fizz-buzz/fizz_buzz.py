'''A module to return a list of numbers in the 'FizzBuzz' manner
   from a given range'''

def fizzbuzz(start, end):
    '''Return a list representing the range of numbers from start
       parameter up to end parameter inclusive with the exception
       of numbers that are divizible by 3 or 5 or both'''
    result = []

    for num in range(start, end + 1):
        if num % 5 == 0:
            if num % 3 == 0:
                result.append('FizzBuzz')
                continue
            result.append('Buzz')
            continue
        if num % 3 == 0:
            result.append('Fizz')
            continue
        result.append(num)

    return result
