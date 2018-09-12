from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import random
import requests

ledPinOne = 3
ledPinTwo = 4
ledPinThree = 5
ledPinFour = 6
ledPinFive = 2

buttonState = 0

GET_TIME_INTERVAL_URL = "http://192.168.1.6:5000/timeInterval"
GET_TARGET_NUMBER_URL = "http://192.168.1.6:5000/targetNumber"
 
try:
	connection = SerialManager()
	a = ArduinoApi(connection = connection)
except:
	print("Failed to connect to Arduino")

#Setup the pinModes
a.pinMode(ledPinOne, a.OUTPUT)
a.pinMode(ledPinTwo, a.OUTPUT)
a.pinMode(ledPinThree, a.OUTPUT)
a.pinMode(ledPinFour, a.OUTPUT)
#a.pinMode(buttonPin, a.INPUT)


def setPinModes(theArduino,theBinaryNum):
	if theBinaryNum[0] == '1': 
		theArduino.digitalWrite(ledPinOne, theArduino.HIGH)
	else:
		theArduino.digitalWrite(ledPinOne, theArduino.LOW)
		

	if theBinaryNum[1] == '1': 
		theArduino.digitalWrite(ledPinTwo, theArduino.HIGH)
	else:
		theArduino.digitalWrite(ledPinTwo, theArduino.LOW)

	
	if theBinaryNum[2] == '1': 
		theArduino.digitalWrite(ledPinThree, theArduino.HIGH)
	else:
		theArduino.digitalWrite(ledPinThree, theArduino.LOW)


	if theBinaryNum[3] == '1': 
		theArduino.digitalWrite(ledPinFour, theArduino.HIGH)
	else:
		theArduino.digitalWrite(ledPinFour, theArduino.LOW)

	if theBinaryNum[4] == '1': 
		theArduino.digitalWrite(ledPinFive, theArduino.HIGH)
	else:
		theArduino.digitalWrite(ledPinFive, theArduino.LOW)




try:
	while True:
		#buttonState = a.digitalRead(buttonPin)
		print("running.")

		#targetNum = int(requests.get(GET_TARGET_NUMBER_URL).text)
		targetNum = 20

		for num in range(0,targetNum): 
			#randomTime=(random.randrange(0,500))/100.00
			#randomTime=requests.get(GET_TIME_INTERVAL_URL).text
			randomTime=0.25
			print("Time interval: %s seconds" % randomTime)
			setPinModes(a,'{0:05b}'.format(num))
			sleep(float(randomTime))
except:
	a.digitalWrite(ledPinOne, a.HIGH)
	a.digitalWrite(ledPinTwo, a.HIGH)
	a.digitalWrite(ledPinThree, a.HIGH)
	a.digitalWrite(ledPinFour, a.HIGH)
	a.digitalWrite(ledPinFive, a.HIGH)


