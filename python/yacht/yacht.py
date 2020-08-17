"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

def _YACHT(dice):
	if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
		return 50
	else:
		return 0

def _ONES(dice):
	return 1 * dice.count(1)

def _TWOS(dice):
	return 2 * dice.count(2)

def _THREES(dice):
	return 3 * dice.count(3)

def _FOURS(dice):
	return 4 * dice.count(4)

def _FIVES(dice):
	return 5 * dice.count(5)

def _SIXES(dice):
	return 6 * dice.count(6)

def _FULL_HOUSE(dice):
	dice.sort()
	countL = dice.count(dice[0])
	countR = dice.count(dice[4])
	if (countL == 2 and countR == 3) or (countL == 3 and countR == 2):
		return sum(dice)
	else:
		return 0

def _FOUR_OF_A_KIND(dice):
	dice.sort()
	countL = dice.count(dice[0])
	countR = dice.count(dice[4])
	if countL == 4 or countL == 5:
		return dice[0] * 4
	elif countR == 4 or countR == 5:
		return dice[4] * 4
	else:
		return 0

def _LITTLE_STRAIGHT(dice):
	dice.sort()
	if dice[0] == 1 and dice[1] ==  2 and dice[2] == 3 and dice[3] == 4 and dice[4] == 5:
		return 30
	else:
		return 0

def _BIG_STRAIGHT(dice):
	dice.sort()
	if dice[0] == 2 and dice[1] ==  3 and dice[2] == 4 and dice[3] == 5 and dice[4] == 6:
		return 30
	else:
		return 0

def _CHOICE(dice):
	return sum(dice)

def _category_dispatcher(dice, category):
	dispatcher = {
		YACHT : _YACHT,
		ONES : _ONES,
		TWOS : _TWOS,
		THREES : _THREES,
		FOURS : _FOURS,
		FIVES : _FIVES,
		SIXES : _SIXES,
		FULL_HOUSE : _FULL_HOUSE,
		FOUR_OF_A_KIND : _FOUR_OF_A_KIND,
		LITTLE_STRAIGHT : _LITTLE_STRAIGHT,
		BIG_STRAIGHT : _BIG_STRAIGHT,
		CHOICE : _CHOICE,
	}
	
	function = dispatcher.get(category, lambda x: "Invalid Category!")
	return function(dice)

def score(dice, category):
    return _category_dispatcher(dice, category)
	
