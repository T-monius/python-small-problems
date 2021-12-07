'''A module for working with float and string representations
   of angles'''

def dms(angle):
    '''Convert a float representing an angle to a string representing
       the degrees, minutes, and seconds of that angle'''
    degrees = str(int(angle))
    rem = angle % 1
    minutes = rem * 60
    rem = minutes % 1
    seconds = rem * 60
    minutes = str(int(minutes)).zfill(2)
    seconds = str(int(seconds)).zfill(2)

    return f"{degrees}°{minutes}'{seconds}\""
