'''A module that implements a simple stack-and-register based
   programming language'''

def print_to_mini_output(mini_output, val):
    '''Print a value to the mini_output'''
    str_val = str(val)
    if len(mini_output) > 0:
        mini_output += f' {str_val}'
    else:
        mini_output += str_val

    return mini_output


def is_negative_numeric(num):
    '''Determine if a string contains only a negative number'''
    return num[0] == '-' and num[1:].isnumeric()


def add(val, other_val):
    '''Add a value to another'''
    return other_val + val


def subtract(val, other_val):
    '''Subtract a value from another'''
    return other_val - val


def multiply(val, other_val):
    '''Multiply a value by another'''
    return other_val * val


def divide(val, other_val):
    '''Return division of a value from another if val is not zero'''
    if other_val > 0:
        return int(other_val / val)

    return None


def modulus(val, other_val):
    '''Return the modulus of a value from another if val is not zero'''
    if other_val > 0:
        return other_val % val

    return None


def compute(val, other_val, command):
    '''Calculate a result operating on two values with a given command'''
    computations = {
        'ADD': add,
        'SUB': subtract,
        'MULT': multiply,
        'DIV': divide,
        'MOD': modulus,
    }
    result = computations[command](val, other_val)

    return result


def minilang(commands):
    '''A function that operates with a stack and register to implement
       a basic programming language'''
    register = 0
    stack = []
    mini_output = ''

    for command in commands.split():
        if command[0] == 'P':
            if command == 'POP':
                register = stack.pop()
            elif command == 'PUSH':
                stack.append(register)
            elif command == 'PRINT':
                mini_output = print_to_mini_output(mini_output, register)
        elif command.isnumeric() or is_negative_numeric(command):
            register = int(command)
        else:
            val = stack.pop()
            register = compute(val, register, command)

    return mini_output
