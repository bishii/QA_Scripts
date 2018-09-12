import itertools
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
	digitOrder = (19,26,13,5)

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
	

def PrintFourDigits(theNumber):
	#theNumber must be a 4 digit string.  use ' ' for blank, 0 for zero	
	digitOrder = (19,26,13,5)
	for digit in range(4):
		PrintNumber(digit,theNumber[digit])
		GPIO.output(digitOrder[digit],GPIO.LOW)
		sleep(0.001)
		GPIO.output(digitOrder[digit],GPIO.HIGH)

def RingBuzzer(gpioNum, NumberOfRings, LengthOfRing, LengthOfPause):
	for a in range(NumberOfRings):
		GPIO.output(gpioNum, True)
		sleep(LengthOfRing)
		GPIO.output(gpioNum, False)
		sleep(LengthOfRing)

#Push buttons
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Buzzer
GPIO.setup(12,GPIO.OUT)

count=5555

button3Pressed = False
button2Pressed = False
button1Pressed = False

intervalsEnum = (1,2)

intervals = itertools.cycle(intervalsEnum)
theInterval = 1

while True:

	################# Right button (16) -- Subtract
	if GPIO.input(16) == True:
		button3Pressed = False
	else:
		if button3Pressed == False:
			RingBuzzer(12,1,0.01,0.10)
			count -= theInterval
			button3Pressed = True

	################ Middle button (20) -- Add

	if GPIO.input(20) == True:
		button2Pressed = False
	else:
		if button2Pressed == False:
			RingBuzzer(12,2,0.01,0.10)
			count += theInterval
			button2Pressed = True

	################ Left button (21) -- Change Interval

	if GPIO.input(21) == True:
		button1Pressed = False
	else:
		#print("Button Pressed!")
		#print(theInterval)
		if button1Pressed == False:
			theInterval = next(intervals)
			RingBuzzer(12,(intervalsEnum.index(theInterval)+1),0.10,0.10)
			button1Pressed = True
	#print(count)
	PrintFourDigits(str(count).ljust(4,' '))

GPIO.cleanup()
