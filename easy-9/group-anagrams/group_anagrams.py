'''A module for finding and grouping anagrams in a list'''

def grouped_anagrams(words):
    '''Return a list of nested lists of anagrams found in input list'''
    all_anagrams = []
    seen_anagrams = {}

    for idx, word in enumerate(words):
        if seen_anagrams.get(idx):
            continue
        sorted_word_chars = sorted(list(word))
        anagrams = []
        for secondary_idx, secondary_word in enumerate(words):
            if idx == secondary_idx or seen_anagrams.get(secondary_idx):
                continue
            if sorted_word_chars == sorted(list(secondary_word)):
                anagrams.append(secondary_word)
                seen_anagrams[secondary_idx] = True
        if len(anagrams) > 0:
            anagrams.append(word)
            all_anagrams.append(anagrams)

    return all_anagrams
