def _get_list(value):
	factor_list = []

	for number in range(2, value // 2 + 1):
		if value % number == 0:
			factor_list.append(number)
			return factor_list + _get_list(value // number)

	return [value]

def factors(value):
	facts = _get_list(value)
	if value in facts and value != 2:
		facts.remove(value)

	return facts