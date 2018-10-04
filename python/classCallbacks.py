from threading import Thread
import time

class Manager():

	def pause_then_die(self):
		MyThread(self.on_thread_finished).start()

	def on_thread_finished(self, data):
		print("on_thread_finished:", data)


class MyThread(Thread):

	myid = 0

	def __init__(self, callback):
		Thread.__init__(self)
		self.callback = callback
		MyThread.myid += 1

	def run(self):
		time.sleep(5)
		data = "hello! Current population is: %s" % MyThread.myid
		self.callback(data)