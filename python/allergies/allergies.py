allergens = [
	'eggs',
	'peanuts',
	'shellfish',
	'strawberries',
	'tomatoes',
	'chocolate',
	'pollen',
	'cats'
]

class Allergies:

	def _decimal_to_binary(self, decimal):
		bits = []
		while decimal:
			bits.append(decimal%2)
			decimal = decimal // 2
		return bits

	def _build_allergy_list(self, score):
		allergy_list = []
		is_allergic_list = self._decimal_to_binary(score)
		if len(is_allergic_list) > len(allergens):
			is_allergic_list = is_allergic_list[:len(allergens)]
		for allergen, is_allergic in zip(allergens, is_allergic_list):
			if is_allergic:
				allergy_list.append(allergen)
				
		return allergy_list
		

	def __init__(self, score):
		self.allergy_list = self._build_allergy_list(score)

	def allergic_to(self, item):
		return item in self.allergy_list

	@property
	def lst(self):
		return self.allergy_list