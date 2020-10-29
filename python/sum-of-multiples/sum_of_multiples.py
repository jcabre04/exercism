import itertools

def sum_of_multiples(limit, multiples):
	set_of_multiples = set()

	for multiple in multiples:
		for num in range(1, limit):
			if multiple and num >= multiple and num % multiple == 0:
				set_of_multiples.add(num)

	'''
	[[set_of_multiples.add(num) for num in range(1, limit) 
		if multiple and num >= multiple and num % multiple == 0] 
			for multiple in multiples]
	'''
	'''
	list_product = list(itertools.product(multiples, list(range(1, limit))))
	[set_of_multiples.add(num) for multiple, num in list_product
		if multiple and num >= multiple and num % multiple == 0]
	'''

	return sum(set_of_multiples) 
	
	
print(sum_of_multiples(10, [7, 5]))