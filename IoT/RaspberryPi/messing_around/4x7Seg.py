import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#segments = (7,8,25,23,18,4,10,11)
#segments = (26,24,16,12,7,19,23,10)
#segments=(26,24,22,16,12,7,19,23)
segments=(23,26,19)

for segment in segments:
	print(segment)
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, 1)

#digits = (24,17,27,22)
digits = (18,11,13,15)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, 1)

input("waiting...")

segments = (26,24,16,12,7,19,23,10)


for segment in segments:
	print(segment)
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, 0)

#digits = (24,17,27,22)
digits = (18,11,13,15)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, 0)
