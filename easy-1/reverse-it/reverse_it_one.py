def reverse_sentence(phrase):
	if len(phrase) < 1 or phrase.isspace():
		return ''

	words = phrase.split(' ')
	words.reverse()
	return ' '.join(words)
