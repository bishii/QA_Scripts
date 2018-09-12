from RPi import GPIO
from time import sleep
import json
import requests
import random
from itertools import cycle
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments=(6,3,0,4,11,9,10,22)
led=17
segmentOrder = (11,4,10,9,6,3,0)
segmentPeriod = 22
digitOrder = (19,26,13,5)

segmentNeighborMatrix = {}

#Top: 10 = go left a digit; 11 = go right a digit
segmentNeighborMatrix[0] = (1,5,10,11)

segmentNeighborMatrix[1] = (0,6)

segmentNeighborMatrix[2] = (1,2,6)

#bottom: 10 = go left a digit; 11 = go right a digit
segmentNeighborMatrix[3] = (2,4,10,11)

segmentNeighborMatrix[4] = (3,5,6)

segmentNeighborMatrix[5] = (0,4,6)

foodDisplayList = [1,1,1,1]

#middle: 10 = go left a digit; 11 = go right a digit
segmentNeighborMatrix[6] = (1,2,4,5,10,11)

foodDisplayList = [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW]


def setGPIO(setTo = False):
	if setTo:
		return GPIO.HIGH
	else:
		return GPIO.LOW

def getAntDelayAmount():
	return random.randrange(100) 

def InitializeAllSegments(initializeTo):
	for a in list(segmentOrder) + [segmentPeriod]:
		GPIO.setup(a,GPIO.OUT)
		GPIO.output(a,setGPIO(initializeTo))
		sleep(0.10)

def InitializeFood():
	#foodDisplayList = [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH] 
	global foodDisplayList
	foodDisplayList = [GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW] 
	

def InitializeAllDigitBits(initializeTo = False):
	for digit in digitOrder:
		GPIO.setup(digit, GPIO.OUT)
		GPIO.output(digit, setGPIO(initializeTo))

def SetAllDigits(setTo = False):
	for x in digitOrder:
		GPIO.output(x,setGPIO(setTo)) 

def SetAllSegments(setTo = False):
	for x in list(segmentOrder) + [segmentPeriod]:
		GPIO.output(x,setGPIO(setTo))

def SingleDigitPlay(digitNumber, segmentIndex):

	#Turn OFF all digits.
	SetAllDigits(True)

	theSegment = segmentOrder[segmentIndex]
	theDigitGPIO = digitOrder[digitNumber]

	#Turn off all segments on all digits
	SetAllSegments(False)

	#Display all four digits (3 will be blank)	
	for digit in range(4):
		if digit == digitNumber:	
			#queue up the ant segment
			GPIO.output(segmentOrder[segmentIndex], GPIO.HIGH)

		else:
			SetAllSegments(False)

		DisplayDots(digit)

		#flash the digit real quick.
		GPIO.output(digitOrder[digit], GPIO.LOW)
		sleep(0.001)
		GPIO.output(digitOrder[digit], GPIO.HIGH)
		


##############STARTING INITIALIZATION#############
# Initialize the 4 digit-bits.

InitializeAllDigitBits()
#input("1. 4 digit bits have been disabled")

InitializeAllSegments(True)
#input("2. All segments have been turned on...")

#for segment in list(segmentOrder) + [segmentPeriod]:
#	GPIO.output(segment, GPIO.LOW)

#input("3. All segments have been turned off...")



def RotateAllSegments():
	for a in segmentOrder:
		GPIO.output(a,GPIO.LOW)
		sleep(1)

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

def DisplayDots(theDigit):
	GPIO.output(22,foodDisplayList[theDigit])

def SignifyNewSession(theNumOfMoves, theNumCompletions):
	for x in range(5):
		for a in range(100):
			PrintFourDigits(theNumOfMoves)

		for a in range(100):
			PrintFourDigits(theNumCompletions)
			

def getNextPosition(theCurrentDigitIndex,theCurrentSegmentIndex):

	GO_LEFT_DIGIT_CODE = 10
	GO_RIGHT_DIGIT_CODE = 11
	
	returnDigit = theCurrentDigitIndex

	options = segmentNeighborMatrix[currentSegmentIndex]

	nextSegmentStep = random.choice(options)
	returnSegment = nextSegmentStep

	if nextSegmentStep == GO_LEFT_DIGIT_CODE:
		#print("Going left!")
		returnDigit -= 1
		if returnDigit == -1:
			returnDigit = len(digitOrder) - 1
		returnSegment = theCurrentSegmentIndex
		#print("new left digit: %s" % returnDigit)

		#Check if food should be eaten... (decimal)
		if currentSegmentIndex == 3: #only on bottom segment...
			if foodDisplayList[returnDigit] == GPIO.HIGH:
				foodDisplayList[returnDigit] = GPIO.LOW 
	
	if nextSegmentStep == GO_RIGHT_DIGIT_CODE:
		#print("Going right!")
		returnDigit += 1
		if returnDigit == len(digitOrder):
			returnDigit = 0
		returnSegment = theCurrentSegmentIndex

		#Check if food should be eaten... (decimal)
		if theCurrentSegmentIndex == 3: #only on bottom segment...
			if foodDisplayList[theCurrentDigitIndex] == GPIO.HIGH:
				foodDisplayList[theCurrentDigitIndex] = GPIO.LOW 
	return (returnDigit, returnSegment)

stocks = {}
ans=input("Ready?")

#Proximity Sensor
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.IN)

#Servo
GPIO.setup(2,GPIO.OUT)

GPIO.output(25,False)


GPIO.setup(12,GPIO.OUT)

print("Waiting for sensor to settle.")

time.sleep(2)

#Servo initialize to 50Hz(?)
p=GPIO.PWM(2,50)
p.start(2.5)

print("Starting now.")
while True:
	GPIO.output(25, True)
	time.sleep(0.00001)
	GPIO.output(25, False)

	#print("before pulse start")  # debug statement
	pulse_start = time.time()
	while GPIO.input(8)==0:
		#print("START!!!")
		pulse_start = time.time()
	while GPIO.input(8)==1:
		#print("END!!")
		pulse_end = time.time()

	pulseDuration = pulse_end - pulse_start
	distance=pulseDuration*17150
	distance = round(distance, 2)
	print("Distance: %s cm" % distance)
	PrintFourDigits(str(distance).split('.')[0].rjust(4,' '))

	if (distance >= 30) and (distance < 60):
		GPIO.output(12,GPIO.HIGH)
		sleep(0.1)
		GPIO.output(12,GPIO.LOW)

		p.ChangeDutyCycle((distance-30)*(12.5/30))
		time.sleep(0.5)
	
GPIO.cleanup()
