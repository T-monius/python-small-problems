'''A module for working with lists of strings'''
import re

def remove_vowels(words):
    '''Remove vowels aeiou from each word in a list'''
    return [re.sub('[aeiouAEIOU]', '', word) for word in words]
