verses = ["a Partridge in a Pear Tree.",
		"two Turtle Doves",
		"three French Hens",
		"four Calling Birds",
		"five Gold Rings",
		"six Geese-a-Laying",
		"seven Swans-a-Swimming",
		"eight Maids-a-Milking",
		"nine Ladies Dancing",
		"ten Lords-a-Leaping",
		"eleven Pipers Piping",
		"twelve Drummers Drumming"]

days = ["first",
		"second",
		"third",
		"fourth",
		"fifth",
		"sixth",
		"seventh",
		"eighth",
		"ninth",
		"tenth",
		"eleventh",
		"twelfth"]

starting_line = "On the {day} day of Christmas my true love gave to me:"

def recite(start_verse, end_verse):
	lines = []
	for verse in range(start_verse - 1, end_verse):
		if verse == 0:
			lines.append(starting_line.format(day=days[verse]) + " " + verses[verse])
		else:
			line = starting_line.format(day=days[verse])
			while verse >= 0:
				if verse == 0:
					line += " and " + verses[verse]
					verse -= 1
				else:
					line += " " + verses[verse] + ","
					verse -= 1
			lines.append(line)
	return lines
