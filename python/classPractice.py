class practice:

	hiddenValue = "me!"

	def __init__(self, id):
		self.myID = id

	def __del__(self):
		print("I'm dying.  Good Bye. Love %s" % self.name)

	def changeHiddenValue(self, theVal):
		practice.hiddenValue = theVal
		return True

	def printHiddenValue(self):
		print(practice.hiddenValue)
		return True