from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from dot import Dot
from random import randrange
import random


FALSE_MIN = 50
FALSE_MAX = 51

TRUE_MIN = 1 
TRUE_MAX = 2 

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, height=8, width=32, block_orientation=-90, rotate=2)
device.contrast(0)

def bubble_once(theList):
    for x in range(len(theList) - 1):
	#sleep(0.0001)
	render_dots()
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

    print [int(o.IntervalTimeTrue * 100) for o in theList]

def bubble_all(theList):

    for x in range(len(theList)):
        bubble_once(theList)
        print x

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



# numDots = int(input("How many Dots ?"))

while True:

	numDots = random.choice([32,64,96,128])

	################################
	## CREATE DOT INSTANCES       ##
	################################

	dotsSource = []
	dotsSourceOrig = []

	row = -1
	for co in range(numDots):
		count = co%32 
		if count == 0: row +=1
		l1 = randrange(FALSE_MIN,FALSE_MAX,1)*0.01
		#l2 = randrange(TRUE_MIN,TRUE_MAX,1)*0.10
		l2 = random.choice([0.10, 0.20, 0.30, 0.40, 0.50])
		theDot = Dot(("dot-instance-%s" % count,l1,l2, (count,row)))
		dotsSource.append(theDot)
		dotsSourceOrig.append(theDot)

	################################
	## END CREATE DOT INSTANCES   ##
	################################

	for duration in range(5000):
		#sleep(0.01)

		render_dots()

		if duration == 500:
			bubble_all(dotsSource)	
