import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

segments=(26,24,22,16,12,18,7,11,13,19,23,15)
#segments=(7,8,25,23,18,24,4,17,27,10,11,22)

for segment in segments:
	print(segment)
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, GPIO.HIGH)

raw_input("waiting...")
