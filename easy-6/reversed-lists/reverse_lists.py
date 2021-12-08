'''A module for working with lists'''

def reverse_in_place(lst):
    '''Mutate the elements of an input list to be the reverse order of
       input'''
    idx1 = 0
    idx2 = len(lst) - 1

    while idx1 < idx2:
        first_element = lst[idx1]
        second_element = lst[idx2]
        lst[idx1] = second_element
        lst[idx2] = first_element
        idx1 += 1
        idx2 -= 1

    return lst
