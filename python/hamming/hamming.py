def _raise_diff_lengths():
	raise ValueError("Require DNA strands of the same length.")

def gut_instinct(strand_a, strand_b):
	hamCount = 0
	for a, b in zip(strand_a, strand_b):
		if a != b:
			hamCount += 1

	return hamCount

def bit_more_nuance(strand_a, strand_b):
	return sum([1 for a, b in zip(strand_a, strand_b) if a != b ])

def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		_raise_diff_lengths()

	#return gut_instinct(strand_a, strand_b)
	
	return bit_more_nuance(strand_a, strand_b)
