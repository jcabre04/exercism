def is_valid(isbn):
	isbn = isbn.replace("-", "")
	indi = [char for char in isbn]

	if len(indi) != 10:
		return False

	if indi[-1] == "X":
		indi[-1] = 10

	for num in indi:
		try:
			int(num)
		except:
			return False

	x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = [int(i) for i in indi]

	return (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) % 11 == 0