EARTH_YEAR_IN_SECONDS = 31557600
MER_YEAR_TO_EARTH = 0.2408467
VEN_YEAR_TO_EARTH = 0.61519726
MAR_YEAR_TO_EARTH = 1.8808158
JUP_YEAR_TO_EARTH = 11.862615
SAT_YEAR_TO_EARTH = 29.447498
URA_YEAR_TO_EARTH = 84.016846
NEP_YEAR_TO_EARTH = 164.79132

class SpaceAge:
	def __init__(self, seconds):
		self.age = seconds

	# may want to change the way rounding works in the future
	def _round_age(self, age):
		return round(age, 2)

	def on_earth(self):
		return self._round_age(self.age / EARTH_YEAR_IN_SECONDS)
		
	def on_mercury(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * MER_YEAR_TO_EARTH))
		
	def on_venus(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * VEN_YEAR_TO_EARTH))
		
	def on_mars(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * MAR_YEAR_TO_EARTH))
		
	def on_jupiter(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * JUP_YEAR_TO_EARTH))
		
	def on_saturn(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * SAT_YEAR_TO_EARTH))
		
	def on_uranus(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * URA_YEAR_TO_EARTH))
		
	def on_neptune(self):
		return self._round_age(self.age / (EARTH_YEAR_IN_SECONDS * NEP_YEAR_TO_EARTH))
		
	