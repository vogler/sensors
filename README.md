# Log sensor data using RPi
Example: https://thingspeak.com/channels/321821
## Sensors
- BME280: temperature, pressure, humidity
- TSL2561: visible light, infrared

## Setup
Use `pipenv install` or
~~~
pip install Adafruit-GPIO
pip install tsl2561
~~~
Register at www.thingspeak.com and replace `Config.key` in `thingspeak.py`.

## Run
~~~
python thingspeak.py 2>&1 | tee -a thingspeak.log
~~~
