def get_factors(number):
	if number <= 0:
		raise ValueError(r".+")

	factors = []
	for fact in range(1,number):
		if number % fact == 0:
			factors.append(fact)
	return factors

def aliquot_sum(number):
	return sum(get_factors(number))

def classify(number):
	al_sum = aliquot_sum(number)
	
	if al_sum == number:
		return "perfect"
	elif al_sum > number:
		return "abundant"
	else:
		return "deficient"
