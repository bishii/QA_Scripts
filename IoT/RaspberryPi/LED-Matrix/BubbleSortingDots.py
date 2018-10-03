from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from dot import Dot
from random import randrange
from RPi import GPIO
import random


FALSE_MIN = 30
FALSE_MAX = 31

TRUE_MIN = 40 
TRUE_MAX = 50 

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, height=8, width=32, block_orientation=-90, rotate=2)
device.contrast(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dotsVariants = [32,64,100,96,128,160,256]

def check_button_events(listOfButtonsGPIOsToheck):
	resp = []
	for b in listOfButtonsGPIOsToheck:
		input_state = GPIO.input(b)
		resp.append((b,input_state))
	return resp
	



class ButtonPressEvent(Exception):
	pass

def bubble_once(theList):

    try:
	    for x in range(len(theList) - 1):
		#sleep(0.0001)
		render_dots()
		button = check_button_events([2])
		if button[0][1] == 1:
			raise ButtonPressEvent("Button pressed by user!")
			
		#print "List length: %s. Currently at: %s - %s" % (len(theList), theList[x].IntervalTimeTrue, \
		#	theList[x+1].IntervalTimeTrue)
		if theList[x].IntervalTimeTrue > theList[x + 1].IntervalTimeTrue:
		    #print "Swapping at position: %s" % x

		    # swap the coordinates of the 2 dots on the board... 
		    temp = theList[x].get_coords()
		    theList[x].move_to(theList[x + 1].get_coords())
		    theList[x + 1].move_to(temp)

		    # then, swap the positions of the two objects in the list!
		    temp = theList[x]
		    theList[x] = theList[x + 1]
	            theList[x + 1] = temp
    except ButtonPressEvent:
	print "Fyi: User pressed button."
	raise

    #print [int(o.IntervalTimeTrue * 100) for o in theList]

def bubble_all(theList):

    try:
        for x in range(len(theList)):
	    bubble_once(theList)
	    print x
    except ButtonPressEvent:
	print "STOPPED in Bubble ALL!!!!"
	raise
	

def render_dots():
        whiteDots = []
        blackDots = []
        with canvas(device) as draw:
                for theDot in dotsSource:
                        if theDot.get_current_state() == True:
                                whiteDots.append(theDot.get_coords())
                        else:
                                blackDots.append(theDot.get_coords())
                draw.point(blackDots,fill="black")
                draw.point(whiteDots,fill="white")

def create_dot_instances(numDots):
	################################
	## CREATE DOT INSTANCES       ##
	################################

	dS = []
	dSO = []

	row = -1
	for co in range(numDots):
		count = co%32 
		if count == 0: row +=1
		l1 = randrange(FALSE_MIN,FALSE_MAX,1)*0.01
		l2 = randrange(TRUE_MIN,TRUE_MAX,1)*0.01
		#l2 = random.choice([0.10, 0.20, 0.30, 0.40, 0.50])
		theDot = Dot(("dot-instance-%s" % count,l1,l2, (count,row)))
		dS.append(theDot)
		dSO.append(theDot)
	return (dS, dSO)


while True:
	try:
		#numDots = int(input("How many Dots ?"))
		numDots = random.choice(dotsVariants)
		dotsSource, dotsSourceOrig = create_dot_instances(numDots)

		for duration in range(5000):

			render_dots()
			y = check_button_events([2])
			if y == False:
				raise ButtonPressEvent("Button was pressed, and bubbled up!")

			if duration == 3000:
				bubble_all(dotsSource)	
	except ButtonPressEvent:
		print "restarting because of button press!"	
