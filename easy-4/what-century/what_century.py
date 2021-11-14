'''A module for dealing with numbers that represent centuries'''

def century_count(numeric_year):
    """Determine the centuries in a numeric year"""
    centuries = None

    if numeric_year % 100 == 0:
        centuries = int(numeric_year / 100)
    else:
        centuries = int(numeric_year / 100) + 1

    return centuries

def get_suffix(numeric_year):
    num = numeric_year % 100
    num = (num % 10 if num > 19 else num)

    if num > 3 or num == 0:
        return 'th'
    elif num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'


def what_century(numeric_year):
    """Convert a numeric year into a readable century figure"""
    centuries = century_count(numeric_year)
    return f'{centuries}{get_suffix(centuries)}'
