def _build_word_dictionary(word):
	dictionary = {}
	for char in word:
		if char not in dictionary:
			dictionary[char] = 1
		else:
			dictionary[char] += 1
			
	return dictionary

def find_anagrams(word, candidates):
	anagrams = []
	word_dict = _build_word_dictionary(word.lower())

	for potential in candidates:
		# Check word and potential are different but have the same length. Otherwise skip this iteration 
		if potential.lower() == word.lower() or len(potential) != len(word):
			continue
	
		temp_dict = _build_word_dictionary(potential.lower())

		# Check the dictionaries contain the same key:value pairs
		if word_dict == temp_dict:
			anagrams.append(potential)
			
	return anagrams