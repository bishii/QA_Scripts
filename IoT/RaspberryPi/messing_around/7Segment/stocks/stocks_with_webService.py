import RPi.GPIO as GPIO
from time import sleep
import json
import requests

WEB_SERVER_URL = 'http://192.168.1.6:5000'
GET_STOCKS = '/stockSymbols'

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT) #green
GPIO.setup(15,GPIO.OUT) #yellow
GPIO.setup(18,GPIO.OUT) #red1
GPIO.setup(23,GPIO.OUT) #red2
GPIO.setup(24,GPIO.OUT) #red3

leds = [14,15,18,23,24]

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




givenAnswer=input("Ready To Start MAIN ??")


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

while True:
	stocks = {}
	print("Trying...")
	ans = requests.get(WEB_SERVER_URL + GET_STOCKS)
	urlPart = ans.text
	print("Got these from Brents webserver: %s" % urlPart)
	a = requests.get("https://www.alphavantage.co/query?function=BATCH_QUOTES_US&symbols=%s&apikey=KJVUHWV5OUYGNR7K" % urlPart)
	it = str(json.loads(a.content.decode()))
	itJSON = json.loads(a.content.decode())
	
	numStocks=len(urlPart.split(','))
	print("Got %s stocks." % numStocks)

	for count in range(numStocks):
		GPIO.output(leds[count],GPIO.HIGH)

	print("Size of the JSON container: %s" % len(itJSON['Stock Batch Quotes']))
	for x in range(len(itJSON['Stock Batch Quotes'])):
		stocks[itJSON['Stock Batch Quotes'][x]['1. symbol']] = itJSON['Stock Batch Quotes'][x]['5. price']
	print(stocks)

	countDown=numStocks
	for stock in stocks.keys():
		for timer in range(250):
			theStockPrice = stocks[stock]
			PrintFourDigits(theStockPrice[:theStockPrice.find('.')].rjust(4,' ')) 
		sleep(0.50)
		GPIO.output(leds[numStocks-1], GPIO.LOW)
		numStocks -= 1

GPIO.cleanup()
