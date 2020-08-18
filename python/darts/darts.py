from math import sqrt

def score(x, y):
	
	length_from_origin = sqrt(x ** 2 + y ** 2)

	if length_from_origin > 10:
		return 0
	elif length_from_origin > 5:
		return 1
	elif length_from_origin > 1:
		return 5
	else:
		return 10
