'''A module for working with strings'''

def letter_swap(input_str):
    words = input_str.split(' ')
    swapped_words = []

    for word in words:
        if len(word) == 1:
            swapped_words.append(word)
        else:
            first = word[0]
            last = word[-1]
            middle = word[1:-1]

            swapped_words.append(last + middle + first)

    return ' '.join(swapped_words)
