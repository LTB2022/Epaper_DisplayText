import time
import busio
import digitalio
import board
import displayio
import adafruit_il0373
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.il0373 import Adafruit_IL0373

displayio.release_displays()

# This pinout works on a Feather M4 and may need to be altered for other boards.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.D9)
dc = digitalio.DigitalInOut(board.D10)
srcs = digitalio.DigitalInOut(board.D6)    # can be None to use internal memory
rst = None    # can be None to not use this pin
busy = None   # can be None to not use this pin


print("Creating display")
display = Adafruit_IL0373(128, 296, spi,
                          cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs,
                          rst_pin=rst, busy_pin=busy)

display.rotation = 1

print("Draw text")
display.text('hello world', 0, 0, Adafruit_EPD.BLACK)
display.display()
