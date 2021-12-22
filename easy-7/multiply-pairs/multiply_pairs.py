'''A module deriviving a single list of products from multiple lists'''

def multiply_all_pairs(primary, secondary):
    '''Return a list of the products of all pairs found between two
       two input lists'''
    products = []

    for num in primary:
        for secondary_num in secondary:
            product = num * secondary_num
            products.append(product)

    return sorted(products)
