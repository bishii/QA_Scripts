import time

class Dot: 
	def __init__(self, settings=("defaultDot",3,10)):
		"""

		Constructor Inputs:
			settings: tuple of:
				1) descriptive name of instance
				2) FALSE interval (seconds)
				3) TRUE interval (seconds)

		"""
		creationTime = time.time()
		self.dotName = settings[0]
		self.IntervalTimeTrue = settings[2]
		self.IntervalTimeFalse = settings[1]
		self.IntervalStartTime = time.time()
		self.CurrentState = False


	def set_interval_start_time(self):
		self.IntervalStartTime = time.time()

	def get_current_state(self):
		"""
			if current state is TRUE:
				if NOW > STOP INTERVAL TIME, then:
				 	set current state = FALSE
				 	return FALSE
			else:
				if NOW > NEXT INTERVAL START TIME, then:
					if NOW in DURATION OF BLINKING:
						Set current state = TRUE
						set interval_start_time = NOW.
					else:
						set current state = FALSE
		"""

		if self.CurrentState == True:
			if time.time() - self.IntervalStartTime >= self.IntervalTimeTrue:
				self.CurrentState = False
				self.set_interval_start_time()
		else:
			if time.time() - self.IntervalStartTime >= self.IntervalTimeFalse:
				self.CurrentState = True
				self.set_interval_start_time()

		return self.CurrentState




