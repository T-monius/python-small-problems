'''A module for determining running totals in an integer list'''

def running_total(ints):
    total = 0
    totals = []

    for num in ints:
        total += num
        totals.append(total)

    return totals