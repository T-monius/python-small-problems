def reverse_word(word):
	chars = list(word)
	chars.reverse()

	return ''.join(chars)

def reverse_words(phrase):
	words = phrase.split(' ')
	new_words = []

	for word in words:
		if len(word) > 4:
			word = reverse_word(word)

		new_words.append(word)

	return ' '.join(new_words)