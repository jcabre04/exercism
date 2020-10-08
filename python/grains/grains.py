grains = [2 ** num for num in range(64)]

def _raise_invalid_number():
    raise ValueError("Input must be inclusively between 1 and 64")

def square(number):
	if number < 1 or number > 64:
		_raise_invalid_number()
	return grains[number - 1]

def total():
	return sum(grains)
