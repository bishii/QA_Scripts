from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from dot import Dot
from random import randrange
import boto3
import json

serial = spi(port=0, device=0, gpio=noop())
#device = max7219(serial, cascaded=4, block_orientation=-90, rotate=2)
device = max7219(serial, height=8, width=32, block_orientation=-90, rotate=2)
device.contrast(0)

dotsSource = []
dotsSourceOrig = []

sqs = boto3.resource('sqs')
queue = sqs.Queue("http://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events")

res = []
finalList = []
while len(res) == 0:
        res = queue.receive_messages(QueueUrl="http://sqs.us-west-2.amazonaws.com/410936176879/Automation_Events",MaxNumberOfMessages=10,VisibilityTimeout=123,ReceiveRequestAttemptId='string')
        finalList += [msg.body for msg in res]
        if len(finalList) == 0:
            print("Queue is empty.  Retrying in 5 seconds...")
            sleep(5)

stocksFromSqs = json.loads(finalList[0])['stocks']
print(stocksFromSqs)

#dotsSource = [("one",2,2,(0,0)),("two",1,5,(5,0))]
#for dotS in dotsSource:
#	dotsPointers.append(dotS)

numDots = input("Ready to display ?")
#OnRangeLow = int(input("ON time min ?"))
#OnRangeHigh = int(input("ON time max?"))
#OffRangeLow = int(input("OFF time min ?"))
#OffRangeHigh = int(input("OFF time max?"))


dictKeys = stocksFromSqs.keys()
print(dictKeys)
print(len(dictKeys))

count = 0 
row = -1
for co in dictKeys:
	theStock = stocksFromSqs[co]
	print("theStock:%s" %theStock)
	if count == 0: row += 1
	count += 1
	if count%32 == 0: count = 0 
	l1 = int(theStock['low_value']) * 0.01
	l2 = int(theStock['high_value']) * 0.01
	print("count,row: %s,%s" % (count,row))
	theDot = Dot(("dot-instance-%s" % co,l1,l2, (count,row)))
	dotsSource.append(theDot)
	dotsSourceOrig.append(theDot)
dotsPointers = []

#for duration in range(10000):
while True:
        sleep(0.01)
        whiteDots = []
        blackDots = []
        with canvas(device) as draw:
                for theDot in dotsSourceOrig:
                        if theDot.get_current_state() == True:
                                whiteDots.append(theDot.get_coords())
                        else:
                                blackDots.append(theDot.get_coords())
                draw.point(blackDots,fill="black")
                draw.point(whiteDots,fill="white")
