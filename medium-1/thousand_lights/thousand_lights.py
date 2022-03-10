'''A module for working with a series of lights'''

def n_toggled_switches_n_times_from_n(num):
    '''Create a List of booleans representing a 'switch bank' and
       iterate it num times toggling switches divisible by the given
       iteration'''
    switch_bank = [False for num in range(0, num)]

    for walk in range(1, num + 1):
        for idx, switch in list(enumerate(switch_bank)):
            is_flip = (idx + 1) % walk == 0
            if is_flip:
                switch_bank[idx] = not switch

    return switch_bank


def find_switches_that_are_on(switch_bank):
    '''Return a list of numbers representing the position of switches
       that are toggled on in a 'switch bank' comprised of booleans'''
    on_switches = []
    for idx, switch in list(enumerate(switch_bank)):
        if switch:
            on_switches.append(idx + 1)

    return on_switches


def switches_toggled_on_from_toggling_n_switches_n_times(num):
    '''Toggle lights divisible by a given iteration during n
       iterations for n lights; return a list of lights on
       represented by integers corresponding to the position
       of the light.'''
    toggled_switch_bank = n_toggled_switches_n_times_from_n(num)
    on_switches = find_switches_that_are_on(toggled_switch_bank)

    return on_switches
