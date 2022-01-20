'''A module for working with numbers that are doubles'''

def is_double(num):
    '''Return a boolean representing whether or not a number is a
       double; that is, the same comparing left and right sides from
       the middle'''
    str_num = str(num)
    str_len = len(str_num)
    if str_len % 2 != 0:
        return False

    midpoint = int(str_len / 2)
    up_to_mid = str_num[:midpoint]
    after_mid = str_num[midpoint:]

    return up_to_mid == after_mid


def twice(num):
    '''Return a number if it's a double; otherwise, double the vale of
       the input number and return that'''
    if is_double(num):
        return num

    return num * 2
