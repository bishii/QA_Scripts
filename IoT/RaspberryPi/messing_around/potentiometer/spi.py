import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 40
MISO = 35
MOSI = 38
CS   = 36
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while 1:
    adc = mcp.read_adc(0)
    voltage = 3.3*adc/1023
    print("ADC=" + str(adc) + " Voltage=%.3fV" %voltage)
    time.sleep(1)
