from RPi import GPIO
from time import sleep
import json
import requests
import random
from itertools import cycle
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.OUT)

#Servo initialize to 50Hz(?)
p=GPIO.PWM(26,10)
p.start(2.5)

print("Starting now.")
while True:
	try:
		for x in range(90):
			cdc=((x+1.05)*0.02)+0.3
			p.ChangeDutyCycle(cdc)
			time.sleep(0.010)
		sleep(3)
	except KeyboardInterrupt as e:
		print(e)
		GPIO.cleanup()
		print("cleaned...")
		exit()
GPIO.cleanup()
