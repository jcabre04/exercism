def slices(series, length):
	if length > len(series) or length <= 0:
		raise ValueError(f"Desired output too long. series:{series} is not >= length:{length}")
	
	output = []
	while len(series) >= length:
		output.append(series[0:length])
		series = series[1:]

	return output
