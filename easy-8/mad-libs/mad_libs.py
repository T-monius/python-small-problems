'''A module for playing the game "Mad Libs"'''

word_types = ['noun', 'verb', 'adjective', 'adverb']
words = {}

for word_type in word_types:
    article = 'an' if word_type[-1] == 'a' else 'a'
    response = input(f'Enter {article} {word_type}: ')
    words[word_type] = response

print(f"Do you {words.get('verb', '')} your {words.get('adjective', '')}\
 {words.get('noun', '')} {words.get('adverb', '')}? That's hilarious!")
