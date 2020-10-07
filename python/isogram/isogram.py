def _loop_with_set(string):
	charExists = set()

	for char in string:
		if char in charExists:
			return False
		else:
			charExists.add(char)

	return True

def is_isogram(string):
	string = string.replace("-", "").replace(" ", "").lower()
	return _loop_with_set(string)