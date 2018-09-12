import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

segments=(6,3,0,4,11,9,10,22)
led=17

for segment in segments:
	print(segment)
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, GPIO.LOW)

GPIO.setup(led, GPIO.OUT)
GPIO.output(led,GPIO.LOW)

GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19,GPIO.LOW)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5,GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.LOW)

input("cleared...")
GPIO.output(led,GPIO.HIGH)

for segment in segments:
	print(segment)
	GPIO.output(segment, GPIO.HIGH)

input("All turned on...")

for segment in segments:
	print(segment)
	GPIO.output(segment, GPIO.LOW)


num = {' ':(0,0,0,0,0,0,0),
	'0':(1,1,1,1,1,1,0),
	'1':(0,1,1,0,0,0,0),
	'2':(1,1,0,1,1,0,1),
	'3':(1,1,1,1,0,0,1),
	'4':(0,1,1,0,0,1,1),
	'5':(1,0,1,1,0,1,1),
	'6':(1,0,1,1,1,1,1),
	'7':(1,1,1,0,0,0,0),
	'8':(1,1,1,1,1,1,1),
	'9':(1,1,1,1,0,1,1)}

# GPIO pin numbers for lookup (immutable)
digits = (11,4,10,9,6,3,0)

givenAnswer=input("What number to display ??")

theDigits = (5,19,26,13)

while True:
	dec = 0


	#Clear All
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(26,GPIO.HIGH)
	GPIO.output(19,GPIO.HIGH)


	#Start
	GPIO.output(5,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)

	GPIO.output(13,GPIO.HIGH)
	GPIO.output(26,GPIO.HIGH)

	GPIO.output(0,GPIO.HIGH) #Center segment
	GPIO.output(9,GPIO.LOW) #Center segment

	sleep(1)

	GPIO.output(5,GPIO.HIGH)
	GPIO.output(19,GPIO.HIGH)

	GPIO.output(13,GPIO.LOW)
	GPIO.output(26,GPIO.LOW)

	GPIO.output(9,GPIO.HIGH) #Center segment
	GPIO.output(0,GPIO.LOW) #Center segment
	
	sleep(1)

GPIO.cleanup()
