from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from dot import Dot

serial = spi(port=0, device=0, gpio=noop())
#device = max7219(serial, cascaded=4, block_orientation=-90, rotate=2)
device = max7219(serial, height=8, width=32, block_orientation=-90, rotate=2)
device.contrast(0)

dotsSource = [("one",2,2,(0,0)),("two",1,5,(5,0))]
dotsPointers = []


for c in dotsSource:
	dotsPointers.append(Dot(c))

for duration in range(1000):
	sleep(0.1)
	whiteDots = []
	blackDots = []
	with canvas(device) as draw:
		for theDot in dotsPointers:
			if theDot.get_current_state() == True:
				whiteDots.append(theDot.get_coords())
			else:
				blackDots.append(theDot.get_coords())	
		draw.point(blackDots,fill="black") 
		draw.point(whiteDots,fill="white") 
	print blackDots
	print whiteDots
