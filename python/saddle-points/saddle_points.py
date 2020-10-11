def _get_col(matrix, col):
	return [row[col] for row in matrix]

def irregularMatrix(matrix):
	row_lens = [len(row) for row in matrix]
	firs_len = row_lens[0]

	for length in row_lens:
		if length != firs_len:
			return True

	return False

def saddle_points(matrix):
	if not matrix:
		return []
	elif irregularMatrix(matrix):
		raise ValueError("The matrix has an irregular shape.")

	saddle_points = []

	for row_index, row in enumerate(matrix):
		for col_index, point in enumerate(row):
			if point == max(row) and point == min(_get_col(matrix, col_index)):
				saddle_points.append({"row":row_index + 1, "column":col_index + 1})

	return saddle_points