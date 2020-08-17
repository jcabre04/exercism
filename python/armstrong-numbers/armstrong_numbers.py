def is_armstrong_number(number):
	armstrong_sum = 0
	for num in str(number):
		armstrong_sum += (int(num) ** len(str(number)))
	return armstrong_sum == number