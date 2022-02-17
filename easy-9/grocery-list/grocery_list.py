'''A module for working with lists of groceries'''

def buy_fruit(groceries_items):
    '''Return a list with the quantity of each product based on a list
       input containing products and their desired quantity'''
    products = []

    for grocery_item in groceries_items:
        product, quantity = grocery_item
        count = 0
        while count < quantity:
            products.append(product)
            count += 1

    return products
