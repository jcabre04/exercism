import re

class PhoneNumber:
	def __init__(self, number):
		number = number.replace("+", "")
		number = number.replace(" ", "")
		number = number.replace("-", "")
		number = number.replace(".", "")
		number = number.replace("(", "")
		number = number.replace(")", "")

		if len(number) == 11 and number[0] == '1':
			number = number[1:]

		if len(number) != 10:
			raise ValueError("Number is not the appropriate length")

		test_letters_in_number = re.match('[a-zA-Z]', number)
		if test_letters_in_number:
			raise ValueError("Number contains letter")

		test_proper_numbers_used = re.match('[2-9][0-9]{2}[2-9][0-9]{6}', number)
		if test_proper_numbers_used is None:
			raise ValueError("Number doesn't follow correct patter")

		self.number = number
		self.area_code = number[:3]

	def pretty(self):
		area_code = self.number[:3]
		part1 = self.number[3:6]
		part2 = self.number[6:]
		return f"({area_code}) {part1}-{part2}"