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


def minilang(commands):
    '''A function that operates with a stack and register to implement
       a basic programming language'''
    cmds = commands.split()
    register = 0
    stack = []
    mini_output = ''

    for command in cmds:
        if command == 'PRINT':
            mini_output = print_to_mini_output(mini_output, register)
        if command == 'ADD':
            val = stack.pop()
            register += val
        if command == 'SUB':
            val = stack.pop()
            register -= val
        if command == 'MULT':
            val = stack.pop()
            register *= val
        if command == 'DIV' and register > 0:
            val = stack.pop()
            register = int(register / val)
        if command == 'MOD':
            val = stack.pop()
            register %= val
        if command == 'POP':
            register = stack.pop()
        if command == 'PUSH':
            stack.append(register)
        if command.isnumeric() or is_negative_numeric(command):
            register = int(command)

    return mini_output
