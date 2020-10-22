def is_isogram(string):
	clean_string = string.replace("-", "").replace(" ", "").lower()
	return len(clean_string) == len(set(clean_string))