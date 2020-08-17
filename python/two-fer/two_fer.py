def two_fer(name=''):
	if name:
		return "One for {name}, one for me.".format(name=name)
	else:
		return "One for you, one for me."