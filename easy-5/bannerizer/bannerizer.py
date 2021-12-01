'''A module for printing formatted messages to standard output'''

def print_outer_line(line_length):
    '''Print a line surrounded by a buffer'''
    print(f'+-{"-" * line_length}-+')


def print_inner_line(line_length=0, msg=''):
    '''Print spaces with a buffer or a message with a buffer'''
    if not msg:
        msg = " " * line_length

    print(f'| {msg} |')


def print_in_box(msg):
    '''Print message with spacing and lines around in a "box"'''
    print_outer_line(len(msg))
    print_inner_line(line_length=len(msg))
    print_inner_line(msg=msg)
    print_inner_line(line_length=len(msg))
    print_outer_line(len(msg))


print_in_box('To boldly go where no one has gone before.')
print('\n')
print_in_box('')
