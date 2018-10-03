import boto3
import time


class Player:
    
	def __init__(self, name, waitBeforePollingSeconds):
		self.name = name
		self.sqs = boto3.resource('sqs')
		self.queue = self.sqs.Queue('https://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events')
		self.res = [['start']]
		self.waitTime = waitBeforePollingSeconds

	def start_polling(self):

		while True:
			res = []
			while len(res) == 0:
				res = self.queue.receive_messages()
			self.res = res


			print("Processed. Deleting current Message.") 
			res[0].delete()


			sendMe = self.append_to_message(self.name)
			self.send_new_message(sendMe)

			print("%s Waiting before proceeding..." % self.name)
			time.sleep(self.waitTime)

			print("%s Got A Message!  it says: %s.  Qutting Now!" \
				% (self.name, self.res[0].body))

	def append_to_message(self, whatToAppend):
		self.oldMessage = self.res[0].body + whatToAppend
		return self.oldMessage 

	def send_new_message(self, whatToSend):
		self.queue.send_message(
			MessageBody=whatToSend)

