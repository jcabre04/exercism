import re

PUNCTUATION = ",!?:&@$%^_."
REPLACEMENT = "           "

def clean_apostrophe(word):
	is_contraction = re.match(r"(\w+'\w+)", word)	
	if is_contraction:
		return is_contraction.groups()[0]
	else:
		return word.replace("\'","")

def count_words(sentence):
	words = sentence.translate(sentence.maketrans(PUNCTUATION, REPLACEMENT)).strip().lower().split()
	count = {}
	for word in words:
		word = clean_apostrophe(word)
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	return count