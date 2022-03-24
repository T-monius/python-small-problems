'''A module for reading files and working with sentences'''
import re

SENTENCE_DELIMETERS = r'[.!?]'

def read_file(filepath):
    '''Return the content of a file based on filepath input'''
    with open(filepath) as file_object:
        content = file_object.read()

    return content

def longest_sentence_with_count(filepath):
    '''Return the longest sentence in a text determined by the filepath
       passed in as an argument returning the count as well'''
    content = read_file(filepath)
    all_sentences = re.split(SENTENCE_DELIMETERS, content)

    longest_sentence = ''
    word_count = 0
    for sentence in all_sentences:
        words = sentence.split()
        current_word_count = len(words)
        if current_word_count > word_count:
            longest_sentence = sentence
            word_count = current_word_count

    return [longest_sentence, word_count]
