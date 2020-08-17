def is_pangram(sentence):
	#The letters we want to check. Can add more in the future
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
	#loop over alphabet. return false if a letter is not present in sentence
	for letter in alphabet:
		if letter not in sentence.lower():
			return False
			
	return True