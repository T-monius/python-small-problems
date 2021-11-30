def counts(input_list):
	'''Derive the count of elements in an input list'''
	occurrences = {}

	for element in input_list:
		is_value_present = occurrences.get(element)

		if is_value_present:
			occurrences[element] += 1
		else:
			occurrences[element] = 1

	return occurrences