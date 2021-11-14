'''A module for working with leap years'''

def is_julian_leap_year(year):
    '''
    Determine whether a year is a leap year according to the Julian
    calendar
    '''
    return year % 4 == 0

def is_leap_year(year):
    '''
    Determine whether a year is a leap year according to the Gregorian
    calendar when adopted by the British Empire.
    '''
    if year < 1752:
        return is_julian_leap_year(year)

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

    return False