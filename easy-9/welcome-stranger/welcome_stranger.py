'''A module for providing welcome output for users'''

def greetings(names, work):
    '''Return a string representing a greeting based on names and
       occupation'''
    name = ' '.join(names)
    title = work.get('title')
    fmt_title = title + ' ' if title else ''
    occupation = work.get('occupation', '')

    return f'Hello, {name}! Nice to have a {fmt_title}{occupation} around.'
