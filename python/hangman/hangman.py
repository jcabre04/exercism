# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		self.word = word
		self.masked_word = "_" * len(self.word)

	def guess(self, char):
		if self.status == STATUS_LOSE:
			raise ValueError("Game is over. You Lost")
		elif self.status == STATUS_WIN:
			raise ValueError("Game is over. You Won")

		if char in self.masked_word:
			self.remaining_guesses -= 1
		elif char in self.word:
			for counter, letter in enumerate(self.word):
				if char == letter:
					word_into_list = list(self.masked_word)
					word_into_list[counter] = char
					self.masked_word = "".join(word_into_list)
		elif self.remaining_guesses == 0:
			self.status = STATUS_LOSE
		else:
			self.remaining_guesses -= 1
			
		if "_" not in self.masked_word:
			self.status = STATUS_WIN

	def get_masked_word(self):
		return self.masked_word

	def get_status(self):
		return self.status
