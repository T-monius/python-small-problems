'''A module for working with lists of numbers'''

def sum_of_sums(nums):
    '''Return a sum of summing all slices of an input list of
       numbers'''
    slices = []
    limit = len(nums) + 1

    for num in range(1, limit):
        current_slice = nums[:num]
        slices.append(current_slice)

    sums = list(map(sum, slices))
    return sum(sums)
