# https://github.com/sim0nx/tsl2561
# sudo pip install Adafruit-GPIO
# sudo pip install tsl2561
from tsl2561 import *

if __name__ == "__main__":
    tsl = TSL2561(gain=TSL2561_GAIN_16X) # autogain=True
    while True:
        # lux = tsl.lux()
        # broadband = visible + infrared
        bb, ir = tsl._get_luminosity()
        lux = tsl._calculate_lux(bb, ir)
        print(lux, bb, ir)
