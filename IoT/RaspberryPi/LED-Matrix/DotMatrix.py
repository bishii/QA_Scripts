from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from dot import Dot
import random

class DotMatrixModule:
	
	def __init__(self):
		self.serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(self.serial, height=8, width=32, block_orientation=-90, rotate=2)
		self.device.contrast(0)

		self.dotsVariants = [32,64,96,128,160,256]

	def check_button_events(self, listOfButtonsGPIOsToheck):
		resp = []
		for b in listOfButtonsGPIOsToheck:
			pass
			#input_state = GPIO.input(b)
			#resp.append((b,input_state))
		return resp

	class ButtonPressEvent(Exception):
		pass
		


	def render_dots(self,theListToRender):
		sleep(0.1)
		whiteDots = []
		blackDots = []
		with canvas(self.device) as draw:
			for theDot in theListToRender:
				if theDot.get_current_state() == True:
					whiteDots.append(theDot.get_coords())
				else:
					blackDots.append(theDot.get_coords())
			draw.point(blackDots,fill="black")
			draw.point(whiteDots,fill="white")


	def create_dot_instances(self,numDots):
		################################
		## CREATE DOT INSTANCES       ##
		################################

		dS = []
		dSO = []
		o = []

		row = -1
		count = 00

		NUM_ROWS=int(numDots / 32)
		HORIZONTAL_SPLITTING=int(random.choice([32,16,8,4]))

		count = 0
		splitCount = 0
		for a in range(NUM_ROWS):
			for b in range(int(32 / HORIZONTAL_SPLITTING)):
				splitCount += 1
				for c in range(HORIZONTAL_SPLITTING):
					o.append(0.10 * splitCount)

		random.shuffle(o)

		for co in range(numDots):
			count = co%32
			if count == 0: row +=1
			#l1 = randrange(FALSE_MIN,FALSE_MAX,1)*0.01
			#l2 = randrange(TRUE_MIN,TRUE_MAX,1)*0.01
			#l2 = random.choice([0.10, 0.20, 0.30, 0.40, 0.50])
			#l2 = random.choice([0.10, 0.20, 0.30, 0.40, 0.50,0.60,0.70,0.80,0.90,1.00])
			#l2 = random.choice([1.0, 0.20, 0.30, 0.40,0.50])
			l1 = random.choice([0.20])
			l2 = o[co]
			theDot = Dot(("dot-instance-%s" % count,l1,l2, (count,row)))
			dS.append(theDot)
			dSO.append(theDot)
		return (dS, dSO)

		return (o,o)
