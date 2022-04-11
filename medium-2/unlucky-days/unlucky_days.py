'''A module for working with Friday the 13ths'''
from datetime import date

FRIDAY = 4

def friday_13th_count(year):
    '''Return the integer count of Fridays in an input year that are
       Friday the 13ths'''
    friday_the_13ths = 0

    for month in range(1, 13):
        thirteenth_of_month = date(year, month, 13)
        if thirteenth_of_month.weekday() == FRIDAY:
            friday_the_13ths += 1

    return friday_the_13ths
