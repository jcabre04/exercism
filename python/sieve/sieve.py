# Given a prime, mark the multiples in the given list with False
# Assumes that the list begins at position 0 and is in order
def setMultiplesTrue(prime, list):
	multiple = prime + prime
	while multiple < len(list):
		list[multiple] = (multiple, False)
		multiple += prime

def primes(limit):
	if limit < 2:
		return []
	
	# Initialize list of tuples representing a number and its prime status
	numbers = [(num, True) for num in range(limit+1)]

	for tuple in numbers:
		if tuple[0] >= 2 and tuple[1] == True:
			setMultiplesTrue(tuple[0], numbers)

	return [num[0] for num in numbers if num[1] == True][2:]

# For quickly running single tests
if __name__ == "__main__":
	print(primes(int(input("Please enter a number:\n"))))
