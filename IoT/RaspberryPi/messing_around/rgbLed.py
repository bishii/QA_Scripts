from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import random
import requests

ledPinOne = 4
ledPinTwo = 5
ledPinThree = 6

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






try:
	while True:
		#buttonState = a.digitalRead(buttonPin)
		print("running.")

		#targetNum = int(requests.get(GET_TARGET_NUMBER_URL).text)
		
		a.analogWrite(ledPinOne, random.randrange(0,255))
		a.analogWrite(ledPinTwo, random.randrange(0,255))
		a.analogWrite(ledPinThree, random.randrange(0,255))
		sleep(1)
except:
	pass


