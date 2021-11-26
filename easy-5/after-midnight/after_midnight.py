'''A module for working with time'''

MINUTES_IN_AN_HOUR = 60
MINUTES_IN_A_DAY = 1440

def after_midnight(timestring):
    '''
    A function for calculating minutes after midnight from an input
    time string
    '''
    hrs, mins = [int(time_part) for time_part in timestring.split(':')]
    if mins == MINUTES_IN_A_DAY:
        return 0

    return mins + (hrs * MINUTES_IN_AN_HOUR)


def before_midnight(timestring):
    '''
    A function for calculating minutes before midnight from an input
    time string
    '''
    mins = after_midnight(timestring)
    if mins == 0:
        return 0

    return MINUTES_IN_A_DAY - mins