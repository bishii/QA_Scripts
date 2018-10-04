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
		distance=input("Enter a number between 30 and 60: ")
		p.ChangeDutyCycle(distance)
		time.sleep(0.5)
	except:
		GPIO.cleanup()
		print("exitting...")
		exit()
GPIO.cleanup()
