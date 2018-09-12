import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

segments=(7,8,25,23,18,24,4,17,27,10,11,22)
#segments=(7,8,25,23,18,4,10,11,22)

for segment in segments:
	print(segment)
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, GPIO.LOW)

input("waiting...")

GPIO.cleanup()
