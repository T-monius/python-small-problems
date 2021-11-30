'''A module for formatting time representations'''

TOTAL_MINUTES_IN_DAY = 1440

def format_num(num):
    '''Conditionally prepend zeros to a string digit to ensure
	   length two'''
    num_char = str(num)
    if len(num_char) < 2:
        return f'0{num_char}'

    return num_char

def time_of_day(minute_time):
    '''Convert negative or positive minute input to 24 hr time'''
    current_mins = minute_time % TOTAL_MINUTES_IN_DAY
    hrs, mins = divmod(current_mins, 60)

    return f'{format_num(hrs)}:{format_num(mins)}'
