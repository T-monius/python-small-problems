'''A module for working with the fibonacci series'''

def find_fibonacci_index_by_length(
    desired_len,
    idx1=1,
    idx2=1,
    current_idx=3,
    ):
    '''Find the index at whish a digit of a given length 'desired_len'
       occurs in the fibonacci series (1 indexed)'''
    val = idx1 + idx2

    if len(str(val)) == desired_len:
        return current_idx

    return find_fibonacci_index_by_length(
        desired_len,
        idx1=idx2,
        idx2=val,
        current_idx=current_idx + 1
    )
