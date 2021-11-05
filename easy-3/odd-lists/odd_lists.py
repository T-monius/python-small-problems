'''A module for selecting elements at odd element positions'''

def odd_element_positions(arbitrary_elements):
    """
    Select elements at odd element positions from a list.
    Element position refers to the list position counting
    from 1 which is opposite of the index. For example,
    element position one is index zero, and element
    position two is index one. The function returns the
    1st, 3rd, 5th, and so on elements from an array
    which correspond to the even indexes.
    """
    idx = 0
    odd_positioned_elements = []

    for el in arbitrary_elements:
        if idx % 2 == 0:
            odd_positioned_elements.append(el)

        idx += 1

    return odd_positioned_elements