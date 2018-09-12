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




givenAnswer=input("What number to display ??")


def clearAllSegments():
	for a in segmentOrder:
		GPIO.output(a,GPIO.LOW)

def PrintNumber(DigitPos1to4, numberToPrint):

	# GPIO pin numbers for lookup (immutable)
	segmentOrder = (11,4,10,9,6,3,0)
	digitOrder = (5,13,26,19)

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
	
	
	#enumerate returns (indexPos, lookup's value)
	for a in enumerate(num[str(numberToPrint)]): 
			if a[1] == 1:
				GPIO.output(segmentOrder[a[0]],GPIO.HIGH)
			else:
				GPIO.output(segmentOrder[a[0]],GPIO.LOW)

	GPIO.output(digitOrder[DigitPos1to4],GPIO.LOW)
	sleep(0.001)
	GPIO.output(digitOrder[DigitPos1to4],GPIO.HIGH)
	

while True:

	PrintNumber(0,4)
	PrintNumber(1,3)
	PrintNumber(2,' ')
	PrintNumber(3,1)

GPIO.cleanup()
