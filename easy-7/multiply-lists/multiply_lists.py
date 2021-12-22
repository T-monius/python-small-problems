'''A module for deriving products of list elements'''

def multiply_lists(primary, secondary):
    '''Return a list of products of similarly indexed elements of two
       lists'''
    products = []
    idx = 0

    for num in primary:
        secondary_num = secondary[idx]
        product = num * secondary_num
        products.append(product)
        idx += 1

    return products
