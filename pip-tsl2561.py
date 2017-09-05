# https://github.com/sim0nx/tsl2561
# sudo pip install Adafruit-GPIO
# sudo pip install tsl2561
from tsl2561 import TSL2561

if __name__ == "__main__":
    tsl = TSL2561(debug=True)
    while True:
        # lux = tsl.lux()
        # broadband = visible + infrared
        bb, ir = tsl._get_luminosity()
        lux = tsl._calculate_lux(bb, ir)
        print(lux, bb, ir)
